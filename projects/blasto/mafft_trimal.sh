#!/bin/bash

fasta="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_cleaned_80.fasta"
aligned="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_cleaned_80_linsi_0_5_realigned.fasta"

mafft --localpair --ep 0 --op 5 --maxiterate 1000 $fasta > $aligned
trimal -in $aligned -out $cleaned -resoverlap 0.80 -seqoverlap 80