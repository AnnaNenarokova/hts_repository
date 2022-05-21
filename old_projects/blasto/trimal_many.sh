#!/bin/bash

al_dir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_aligned_linsi_0/"
cleaned_dir="/Users/anna/work/blasto_local/tRNA/tRNA_phylogeny/tryp_tRNAs_aligned_linsi_0/tryp_tRNAs_cleaned_80/"
mkdir $cleaned_dir
cd $al_dir

for msa in *.fasta
do
    cleaned_msa=$cleaned_dir$msa
    trimal -in $msa -out $cleaned_msa -resoverlap 0.8 -seqoverlap 80
done
