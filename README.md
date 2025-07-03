# Project 01: HTSeq 2.0 Read Counting

**Description:**
This project demonstrates how to use HTSeq 2.0 to count reads mapped to genes from RNA-Seq data. It uses a GTF annotation file and a BAM alignment file as inputs.

**How it works:**
- Reads gene annotation from a GTF file.
- Loads aligned reads from a BAM file.
- Maps reads to genes and counts the number of hits per gene.

**Files:**
- `example.gtf`: Gene annotation file (GTF format).
- `example.bam`: Aligned sequencing reads (BAM format).
- `01_htseq_analysis.py`: Main script to perform counting.

**Requirements:**
- Python
- HTSeq 2.0 (`pip install HTSeq`)

**Note:** Sample files are not included. You need to supply valid `.gtf` and `.bam` files to run this script.
