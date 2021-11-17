#!/bin/bash

msa="/Users/anna/work/euk_local/NCBI_COGs/COG0016_aligned.fasta"
trimmed_msa="/Users/anna/work/euk_local/NCBI_COGs/COG0016_aligned_trimal_08_90.fasta"

trimal -in $msa -out $trimmed_msa -resoverlap 0.8 -seqoverlap 90
