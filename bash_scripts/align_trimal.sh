#!/bin/bash

msa="/Users/anna/work/euk_local/NCBI_COGs/COG0016_aligned_long_gaps.fasta"
trimmed_msa="/Users/anna/work/euk_local/NCBI_COGs/COG0016_aligned_trimal_75.fasta"

trimal -in $msa -out $trimmed_msa -resoverlap 0.75 -seqoverlap 75

outfile="/Users/anna/work/euk_local/NCBI_COGs/COG0016_trimal_75_realigned.fasta"

mafft --op 5 --ep 0 $trimmed_msa > $outfile