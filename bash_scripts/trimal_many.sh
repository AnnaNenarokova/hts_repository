#!/bin/bash

al_dir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tRNAs_fasta_cleaned_0.9/"

cd $al_dir

for msa in *.fasta
do
    trimmed_msa=$msa"_95.fasta"
    trimal -in $msa -out $trimmed_msa -resoverlap 0.95 -seqoverlap 95
done
