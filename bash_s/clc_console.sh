#!/bin/bash
cd /home/anna/bioinformatics/bioprograms/clc-assembly-cell-4.3.0-linux_64
./clc_assembler -o /home/anna/bioinformatics/outdirs/contigs_mut9.fasta --cpus 8 -p fb ss 180 250 -q -i /home/anna/bioinformatics/htses/plasmid70_TGACCA_L001_R1_001.fastq/home/anna/bioinformatics/htses/plasmid70_TGACCA_L001_R2_001.fastq -n