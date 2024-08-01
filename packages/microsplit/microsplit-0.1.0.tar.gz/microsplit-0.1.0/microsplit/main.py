"""
This script is a the Microsplit project, designed to process paired-end FASTQ files by fragmenting DNA sequences at specified restriction enzyme sites.

Copyright © 2024 Samir Bertache

SPDX-License-Identifier: AGPL-3.0-or-later

===============================================================================

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import logging
import os
import re
import signal
import subprocess
import sys
from multiprocessing import Process, Queue

import pysam

# Setup logging
logging.basicConfig(level=logging.INFO)

__version__="0.1.0"

def signal_handler(sig, frame, outF, outR):
    """
    Handle termination signals to gracefully terminate processes.

    Parameters:
        sig (int): Signal number.
        frame (frame object): Current stack frame.
        outF (subprocess.Popen): Process for the forward output.
        outR (subprocess.Popen): Process for the reverse output.
    """
    logging.info(f"\nReceived signal {sig}. Terminating gracefully...")
    outF.terminate()
    outR.terminate()
    sys.exit()


def Partitionning(num_threads):
    """
    Partition the number of threads for writing and fragmenting.
    """
    TWrite = num_threads // 4
    TFrag = num_threads - (TWrite * 2)
    return TWrite, TFrag


def ReadBamFilePair(bam_for_file, bam_rev_file, Input_Queue, TFrag):
    """
    Read simultaneously two BAM files and put read pairs into an input queue.

    Parameters:
        bam_for_file (str): Path to the forward BAM file.
        bam_rev_file (str): Path to the reverse BAM file.
        Input_Queue (Queue): Queue to store read pairs.
        TFrag (int): Number of fragmenting threads.
    """
    with pysam.AlignmentFile(
        bam_for_file, "rb"
    ) as bam_for, pysam.AlignmentFile(bam_rev_file, "rb") as bam_rev:
        for read_for, read_rev in zip(bam_for, bam_rev):
            if read_for and read_rev:
                # Convert read objects to serializable format
                read_for_data = (
                    read_for.query_name,
                    read_for.query_sequence,
                    read_for.query_qualities,
                    read_for.cigarstring,
                )
                read_rev_data = (
                    read_rev.query_name,
                    read_rev.query_sequence,
                    read_rev.query_qualities,
                    read_rev.cigarstring,
                )
                # if read_for_data[0] != read_rev_data[0]:
                # print(read_for_data[0], read_rev_data[0], flush=True)
                if len(read_for_data) == 4 and len(read_rev_data) == 4:
                    Input_Queue.put([read_for_data, read_rev_data])
                else:
                    continue
                # print(read_for_data, flush=True)
        for _ in range(int(TFrag) + 1):
            Input_Queue.put(None)


def OpenOutput(TWrite, output_forward, output_reverse):
    """
    Open output files for writing with pigz compression.

    Parameters:
        TWrite (int): Number of threads for writing.
        output_forward (str): Path to the forward output file.
        output_reverse (str): Path to the reverse output file.

    Returns:
        outF (subprocess.Popen): Process for the forward output.
        outR (subprocess.Popen): Process for the reverse output.
    """
    # Open output files for writing
    outF = subprocess.Popen(
        ["pigz", "-c", "-p", str(TWrite)],
        stdin=subprocess.PIPE,
        stdout=open(output_forward, "wb"),
    )
    outR = subprocess.Popen(
        ["pigz", "-c", "-p", str(TWrite)],
        stdin=subprocess.PIPE,
        stdout=open(output_reverse, "wb"),
    )

    # Register signal handlers
    signal.signal(
        signal.SIGINT,
        lambda sig, frame: signal_handler(sig, frame, outF, outR),
    )  # Ctrl+C
    signal.signal(
        signal.SIGTSTP,
        lambda sig, frame: signal_handler(sig, frame, outF, outR),
    )  # Ctrl+Z

    return outF, outR


def WriteFastQFilePair(Output_Queue, outF, outR, TFrag):
    """
    Write FastQ file pairs to the output using data from the output queue.

    Parameters:
        Output_Queue (Queue): Queue to get processed read pairs.
        outF (subprocess.Popen): Process for the forward output.
        outR (subprocess.Popen): Process for the reverse output.
        TFrag (int): Number of fragmenting threads.
    """
    finished_processes = 0
    while finished_processes < TFrag:
        try:
            data = Output_Queue.get()
            if data is None:
                finished_processes += 1
            else:
                outF.stdin.write("".join(data[0]).encode("utf-8"))
                outR.stdin.write("".join(data[1]).encode("utf-8"))

        except Exception as e:
            logging.error(f"Error in write_pairs: {e}")


def ManagePigzProblems(outF, outR, output_forward, output_reverse):
    """
    Manage pigz process termination and check for errors.
    """
    outF.stdin.close()
    outR.stdin.close()
    outF.wait()
    outR.wait()

    if outF.returncode != 0:
        logging.error(f"Error in pigz command for file {output_forward}")
    if outR.returncode != 0:
        logging.error(f"Error in pigz command for file {output_reverse}")


def TakeCigarTuple(cigar):
    """
    Parse CIGAR string into tuples of operations and lengths.
    """
    cigar_tuples = []

    for match in re.finditer(r"(\d+)([MIDNSHP=X])", cigar):
        length = int(match.group(1))
        op = match.group(2)
        cigar_tuples.append((length, op))

    return cigar_tuples


def CreateFrag(read_data, cigar_tuples, seed_size, LenAdd):
    """
    Extract fragments in the FastQ format from read
    Extract mapped fragments and non mapped fragment

    Parameters:
        read (tuple): The read from which to extract information.
        cigar_tuples (list): A list of tuples representing the CIGAR string.
        seed_size (int): The minimum size of a segment to be considered for extraction.

    Returns:
        tuple: A tuple containing the read name and a list of FastQ format strings.
    """
    Name, sequence, quality, cigar = read_data
    quality_str = "".join(
        chr(q + 33) for q in quality
    )  # Convert quality scores to ASCII characters

    AllRead = []
    mapped_seq = ""
    soft_clipped_seq = ""
    already_mapped = False
    index = 0
    for i, Tuple in enumerate(cigar_tuples):
        length, op = Tuple
        length = int(length)
        if op in ["S", "H"] and i == 0:
            index += length
            continue

        elif op in ["S", "H"]:
            index += length
            continue

        else:
            if len(sequence) != index and (index > seed_size):
                soft_clipped_seq = (
                    Name
                    + "\n"
                    + sequence[0 : index + LenAdd]
                    + "\n"
                    + "+"
                    + "\n"
                    + quality_str[0 : index + LenAdd]
                    + "\n"
                )
                mapped_seq = (
                    Name
                    + "\n"
                    + sequence[index:]
                    + "\n"
                    + "+"
                    + "\n"
                    + quality_str[index:]
                    + "\n"
                )
                already_mapped = True
                AllRead.append(mapped_seq)
                AllRead.append(soft_clipped_seq)
            break

    for i, Tuple in enumerate(cigar_tuples[::-1]):
        length, op = Tuple
        length = int(length)
        if op in ["S", "H"] and i == 0:
            index += length
            continue

        elif op in ["S", "H"]:
            index += length
            continue

        else:
            if len(soft_clipped_seq) != 0 and (index > seed_size):
                soft_clipped_seq = (
                    Name
                    + "\n"
                    + sequence[0 : index + LenAdd]
                    + "\n"
                    + "+"
                    + "\n"
                    + quality_str[0 : index + LenAdd]
                    + "\n"
                )
                mapped_seq = (
                    Name
                    + "\n"
                    + sequence[index:]
                    + "\n"
                    + "+"
                    + "\n"
                    + quality_str[index:]
                    + "\n"
                )

                if not already_mapped:
                    AllRead.append(mapped_seq)
                AllRead.append(soft_clipped_seq)
            break

    return Name, AllRead


def CheckNonData(data):
    for element in data[0]:
        if element is None:
            return False
    for element in data[1]:
        if element is None:
            return False
    return True


def process_items(Input_Queue, Output_Queue, seed_size, LenAdd):
    """
    Process items from the input queue, split the reads based on CIGAR strings, and put the results into the output queue.

    Parameters:
        Input_Queue (Queue): Queue to get read pairs.
        Output_Queue (Queue): Queue to put processed read pairs.
        seed_size (int): The minimum size of a segment to be considered for extraction.
    """

    try:
        while True:
            data = Input_Queue.get()

            if data is None:
                Output_Queue.put(None)
                break

            PassOrNot = CheckNonData(data)

            if data[1][0] != data[0][0]:
                print(data[1][0], data[0][0], flush=True)
                raise ValueError(
                    "Names of two BAM files aren't the same !! Please check your BAM files. "
                )

            if PassOrNot:
                read_for_data, read_rev_data = data
                FastQFor = ""
                FastQRev = ""
                NameRef = ""

                SplitFor = False
                SplitRev = False

                cigarFor = read_for_data[3]
                cigarRev = read_rev_data[3]

                if "S" in cigarFor:
                    NameFor, ListOfFragmentFor = CreateFrag(
                        read_for_data,
                        TakeCigarTuple(cigarFor),
                        seed_size,
                        LenAdd,
                    )
                    SplitFor = True
                    NameRef = NameFor
                else:
                    NameFor = ""
                    ListOfFragmentFor = []

                if "S" in cigarRev:
                    NameRev, ListOfFragmentRev = CreateFrag(
                        read_rev_data,
                        TakeCigarTuple(cigarRev),
                        seed_size,
                        LenAdd,
                    )
                    SplitRev = True
                    NameRef = NameRev
                else:
                    ListOfFragmentRev = []

                if SplitFor or SplitRev:
                    AllFrag = ListOfFragmentFor + ListOfFragmentRev
                    for i, ForRead in enumerate(AllFrag):
                        for j, RevRead in enumerate(AllFrag):
                            # Delete pairs composed by Mapped For and Mapped Rev
                            # Cause already take in account
                            if i > j:
                                FastQFor += (
                                    "@"
                                    + NameRef
                                    + ":"
                                    + str(i)
                                    + str(j)
                                    + ForRead
                                )
                                FastQRev += (
                                    "@"
                                    + NameRef
                                    + ":"
                                    + str(i)
                                    + str(j)
                                    + RevRead
                                )
                else:
                    FastQFor = (
                        read_for_data[0]
                        + "\n"
                        + read_for_data[1]
                        + "\n"
                        + "+"
                        + "\n"
                        + "".join(chr(q + 33) for q in read_for_data[2])
                        + "\n"
                    )
                    FastQRev = (
                        read_rev_data[0]
                        + "\n"
                        + read_rev_data[1]
                        + "\n"
                        + "+"
                        + "\n"
                        + "".join(chr(q + 33) for q in read_rev_data[2])
                        + "\n"
                    )

                if FastQFor and FastQRev:
                    Output_Queue.put((FastQFor, FastQRev))
                    FastQFor = ""
                    FastQRev = ""

    except ValueError as e:
        logging.error(f"Error in process_items: {e}")
        sys.exit()

    finally:
        if len(FastQRev) != 0:
            Output_Queue.put((FastQFor, FastQRev))

        Output_Queue.put(None)


def Communicate(TWrite, TFrag):
    print(
        f"There is {TWrite} write threads per files and {TFrag} fragmenting threads.",
        flush=True,
    )


def EnsureEndding(outF, outR):
    outF.terminate()
    outR.terminate()
    print("Closing done")


def cut(args):
    """
    Main function to orchestrate the reading, processing, and writing of BAM files to FastQ.

    Parameters:
        args (argparse.Namespace): Namespace object containing command-line arguments.
    """
    bam_for_file = args.bam_for_file
    bam_rev_file = args.bam_rev_file
    output_forward = args.output_forward
    output_reverse = args.output_reverse
    num_threads = args.num_threads
    seed_size = args.seed_size
    LenAdd = args.lenght_added

    if not os.path.exists(bam_for_file) or not os.path.exists(bam_rev_file):
        logging.error("BAM file does not exist.")
        sys.exit()

    Input_Queue = Queue()
    Output_Queue = Queue()
    TWrite, TFrag = Partitionning(num_threads)
    outF, outR = OpenOutput(TWrite, output_forward, output_reverse)

    Communicate(TWrite, TFrag)

    # Process for reading bam files
    def read_process():
        ReadBamFilePair(bam_for_file, bam_rev_file, Input_Queue, TFrag)

    # Process for processing items
    def process_process_all():
        process_items(Input_Queue, Output_Queue, seed_size, LenAdd=2)

    # Process for writing pairs
    def write_process():
        WriteFastQFilePair(Output_Queue, outF, outR, TFrag)

    try:
        # Start the processes
        read_p = Process(target=read_process)
        read_p.start()

        process_p_list = [
            Process(target=process_process_all) for _ in range(TFrag)
        ]
        for p in process_p_list:
            p.start()

        write_p = Process(target=write_process)
        write_p.start()

        # Wait for all processes to finish
        read_p.join()

        for p in process_p_list:
            p.join()

        write_p.join()

    except Exception as e:
        logging.error(f"Error in main: {e}")

    finally:
        ManagePigzProblems(outF, outR, output_forward, output_reverse)
        EnsureEndding(outF, outR)


def main_cli():
    parser = argparse.ArgumentParser(description="Process Micro-C BAM files to FastQ.")
    parser.add_argument(
        "--bam_for_file",
        type=str,
        help="Path to forward BAM file.",
        required=True,
    )
    parser.add_argument(
        "--bam_rev_file",
        type=str,
        help="Path to reverse BAM file.",
        required=True,
    )
    parser.add_argument(
        "--output_forward",
        type=str,
        help="Path to output forward FastQ file.",
        required=True,
    )
    parser.add_argument(
        "--output_reverse",
        type=str,
        help="Path to output reverse FastQ file.",
        required=True,
    )
    parser.add_argument(
        "--num_threads",
        type=int,
        help="Total number of threads.",
        required=True,
    )
    parser.add_argument(
        "--seed_size",
        type=int,
        help="Minimum size of a segment for extraction.",
        required=True,
    )
    parser.add_argument(
        "--lenght_added",
        type=int,
        help="Number of base pairs added to the neoformed fragment after completion of soft clipping (Default value is 2)",
        required=True,
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    args = parser.parse_args()
    cut(args)
    
    
if __name__ == "__main__":
    main_cli()
