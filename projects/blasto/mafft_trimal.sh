#!/bin/bash

fasta="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNAs_80_80.fasta"
aligned="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNAs_80_realigned.fasta"
cleaned="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNAs_80_realigned_90_90.fasta"

mafft --op 5 --ep 0 --genafpair --maxiterate 1000 $fasta > $aligned
trimal -in $aligned -out $cleaned -resoverlap 0.90 -seqoverlap 90