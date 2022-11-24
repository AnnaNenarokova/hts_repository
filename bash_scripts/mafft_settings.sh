#!/bin/bash

infile="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNA_trimal_90_Bnonstop.fasta"
outfile="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tryp_tRNA_trimal_90_Bnonstop.fasta_aligned.fasta "

mafft --ep 0 --genafpair --maxiterate 1000 $infile > $outfile