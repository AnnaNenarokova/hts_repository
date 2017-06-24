#!/bin/bash
bam="/home/anna/bioinformatics/blasto/igv_session_p57/RNA_30_junction.bam"
bed="/home/anna/bioinformatics/blasto/rna_cov_analysis/stop_codon_environs.bed"
hist="/home/anna/bioinformatics/blasto/rna_cov_analysis/bed_hist.txt"
bedtools coverage -d -abam $bam -b $bed > $hist
