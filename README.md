# Project 03: SonicParanoid-style Ortholog Inference

**Description:**
This project simulates basic ortholog inference using the concept of reciprocal best hits (RBH), inspired by tools like SonicParanoid.

**How it works:**
- Parses pairwise BLAST output files between species in tabular format.
- Identifies reciprocal best hits as candidate orthologous genes.

**Files:**
- `speciesA_vs_speciesB.tsv`: BLAST results from species A to B.
- `speciesB_vs_speciesA.tsv`: BLAST results from species B to A.
- `03_sonicparanoid_orthologs.py`: Script to infer orthologs using RBH.

**Requirements:**
- Python
- pandas

**Note:** User must provide real BLAST result files in tab-delimited format.
