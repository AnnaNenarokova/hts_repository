#!/bin/bash
breseq -r /home/anna/bioinformatics/outdirs/contigs_mut9.fasta_BL21.fasta/prokka_out/PROKKA_10202014.gbk \
-j 8 -o /home/anna/bioinformatics/outdirs/breseq_mut9_contigs \
/home/anna/bioinformatics/htses/dasha/Ecoli-mut9_trimmed_paired_R1.fastq \
/home/anna/bioinformatics/htses/dasha/Ecoli-mut9_trimmed_paired_R2.fastq