#!/bin/bash

fasta_dir="/Users/anna/work/blasto_local/tRNA/tRNAseq/fasta_results_tRNAseq/tRNA/"
outdir="/Users/anna/work/blasto_local/tRNA/tRNAseq/fasta_results_tRNAseq/tRNA_aligned/"

mkdir $outdir

cd $fasta_dir
for infile in *.fasta
do
	outfile=$outdir$infile
	mafft --localpair --op 10 --ep 0 --maxiterate 1000 $infile > $outfile
done