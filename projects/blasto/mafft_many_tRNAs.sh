#!/bin/bash

fasta_dir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_fastas/"
outdir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tryp_tRNAs_aligned_linsi_0/"

mkdir $outdir

cd $fasta_dir
for infile in *.fasta
do
	outfile=$outdir$infile
	mafft --localpair --ep 0 --maxiterate 1000 $infile > $outfile
done