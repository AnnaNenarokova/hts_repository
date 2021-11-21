#!/bin/bash

fasta="/home/anna/work/blasto_local/tRNA_tree/all_tryp_tRNAs.fasta"
aligned="/home/anna/work/blasto_local/tRNA_tree/all_tryp_tRNAs_linsi_aligned_0_5.fasta"

mafft --localpair --ep 0 --op 5 --maxiterate 1000 $fasta > $aligned
trimal -in $aligned -out $cleaned -resoverlap 0.80 -seqoverlap 80