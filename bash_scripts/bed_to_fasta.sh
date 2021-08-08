#!/bin/bash

# in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_DNA_scaffolds.fa"
# bed="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_only_taa_dist_10.gff"
# out_fasta="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_only_taa_dist_10.fna"

in_fasta="/Users/annanenarokova/work/blasto_local/fasta/p57_DNA_scaffolds.fa"
bed="/Users/annanenarokova/work/blasto_local/p57_annotation.gff"
out_fasta="/Users/annanenarokova/work/blasto_local/fasta/p57_cds.fna"


bedtools getfasta -fi $in_fasta -bed $bed -fo $out_fasta -s
