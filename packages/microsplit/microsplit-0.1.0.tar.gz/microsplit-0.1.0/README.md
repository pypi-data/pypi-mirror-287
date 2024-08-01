<!--
SPDX-FileCopyrightText: 2024 Samir Bertache

SPDX-License-Identifier: CC0-1.0
-->
# Microsplit

Microsplit is a command-line tool designed for processing Micro-C data by identifying and managing chimeric reads in BAM files. It follows the logic and structure of the [Parasplit](https://pypi.org/project/parasplit/) tool but is tailored for Micro-C data. The tool reads alignment files (SAM, BAM, or CRAM) using `pysam` and identifies events of soft-clipping or hard-clipping. The identified clipping points are treated as restriction sites to generate new pairs of sequences.

## Features

- **Parallel Processing**: Microsplit utilizes parallel processing to enhance performance and efficiency.
- **Soft-Clipping and Hard-Clipping Detection**: It detects soft-clipping ('S') and hard-clipping ('H') in CIGAR strings to identify chimeric reads.
- **Fragment Generation**: Generates new fragments by considering the identified clipping points as restriction sites.
- **Error Margin Handling**: Adds a fixed number of base pairs to new fragments to account for potential over-mapping by Bowtie2, ensuring more accurate downstream analysis.
- **Output Paired Reads**: Outputs both end-to-end aligned pairs and newly generated fragment pairs.

## Installation

Microsplit is available on PyPI and can be installed using pip:

```bash
pip install microsplit
```

## Usage

Before using Microsplit, you need to perform an initial alignment of reads using Bowtie2 with the `--local-very-sensitive` mode and the `-xeq` option to obtain explicit CIGAR strings. Below is an example of how to use Microsplit from the command line:

```bash
microsplit --bam_for_file path/to/forward.bam \
           --bam_rev_file path/to/reverse.bam \
           --output_forward path/to/output_forward.fastq.gz \
           --output_reverse path/to/output_reverse.fastq.gz \
           --num_threads 8 \
           --seed_size 20 \
           --length_added 10
```

### Command-Line Arguments

- `--bam_for_file`: Path to the forward BAM file.
- `--bam_rev_file`: Path to the reverse BAM file.
- `--output_forward`: Path to the output forward FastQ file.
- `--output_reverse`: Path to the output reverse FastQ file.
- `--num_threads`: Total number of threads for parallel processing.
- `--seed_size`: Minimum size of a fragment to be generated.
- `--length_added`: Number of base pairs added to the new fragment after soft clipping to account for potential over-mapping by Bowtie2.

## Methodology

Microsplit processes Micro-C data by:

1. **Reading BAM Files**: Reads the forward and reverse BAM files simultaneously.
2. **Identifying Clipping Events**: Identifies soft-clipping and hard-clipping events from the CIGAR strings in the BAM files.
3. **Generating Fragments**: Uses the clipping points as restriction sites to generate new fragments, adding a fixed number of base pairs (`length_added`) to account for potential over-mapping by Bowtie2.
4. **Outputting Paired Reads**: Outputs both end-to-end aligned pairs and the newly generated fragment pairs.

The length added to new fragments helps to handle potential misalignments due to Bowtie2's tendency to over-map reads and not soft-clip enough, ensuring more accurate results.


## License

Microsplit is released under the AGPLv3 license. The code is freely available on [Gitbio](https://gitbio.ens-lyon.fr/LBMC/hub/microsplit).

## Contributing

We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or issues, please contact samir.bertache.djenadi@gmail.com
---

Thank you for using Microsplit!
