#!/bin/bash
bed="/home/anna/bioinformatics/blasto/rna_cov_analysis/stop_codon_environs.bed"
bam="/home/anna/bioinformatics/blasto/igv_session_p57/RNA_30_junction.bam"
out="/home/anna/bioinformatics/blasto/rna_cov_analysis/stop_codon_environs.mpileup"
samtools mpileup -l $bed $bam > $out
