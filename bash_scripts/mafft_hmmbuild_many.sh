#!/bin/bash
cog_dir="/home/anna/work/euk_local/cogs/"

cd $cog_dir
for fasta in *.fa
do
	aligned=$fasta".aligned.fasta"
	mafft $fasta > $aligned
	hmm_file=$fasta".hmm"
	hmmbuild $hmm_file $aligned
done
