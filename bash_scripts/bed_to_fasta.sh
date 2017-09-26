#!/bin/bash

in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_DNA_scaffolds.fa"
bed="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_only_taa_dist_10.gff"
out_fasta="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_only_taa_dist_10.fna"
bedtools getfasta -fi $in_fasta -bed $bed -fo $out_fasta -s #strand
