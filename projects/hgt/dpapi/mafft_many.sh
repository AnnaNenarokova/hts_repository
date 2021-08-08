#!/bin/bash

N=128
(
for fasta in *.fa; do 
   ((i=i%N)); ((i++==0)) && wait
    mafft --localpair --maxiterate 1000 $fasta > $fasta".aln" & 
done
)