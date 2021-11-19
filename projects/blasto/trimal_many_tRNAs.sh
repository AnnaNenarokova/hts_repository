#!/bin/bash

aligned_dir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_aligned/"

cd $aligned_dir

for msa in *.aligned
do
    trimmed_msa=$msa"_80.fasta"
    trimal -in $msa -out $trimmed_msa -resoverlap 0.8 -seqoverlap 80
done
