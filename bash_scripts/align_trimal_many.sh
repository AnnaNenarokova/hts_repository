#!/bin/bash
fasta_folder="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tRNAs_fasta/"
aligned_folder="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/tRNAs_fasta_aligned/"
cd $fasta_folder
for f in *.fasta
do
	echo $f
	aligned=$aligned_folder$f".aligned"
	mafft --quiet $f > $aligned
	trimmed=$aligned".trimmed.fasta"
	trimal -in $aligned -out $trimmed -resoverlap 0.95 -seqoverlap 95
done