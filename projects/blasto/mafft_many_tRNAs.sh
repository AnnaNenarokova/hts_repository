#!/bin/bash

fasta_dir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_aligned/"
outdir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_fastas/"
cd $fasta_dir
for infile in *.fasta
do
	outfile=$outdir$infile
	mafft --op 5 --ep 0 $infile > $outfile
done