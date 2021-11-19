#!/bin/bash

msa="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNAs_aligned.fasta"
cleaned_msa="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNAs_70_10.fasta"
trimal -in $msa -out $cleaned_msa -resoverlap 0.70 -seqoverlap 30