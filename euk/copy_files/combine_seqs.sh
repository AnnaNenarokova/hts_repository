#!/bin/bash

outdir="/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_all/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done

indir="/Users/anna/work/euk_local/nina_markers/fasta_markers/bacteria_manually_cleaned/"
outdir="/Users/anna/work/euk_local/nina_markers/singlehit_results/alpha/be/28_markers_29_09_22/be_alpha_fastas/"
for f in *.faa
do
 echo $f
 infile=$indir$f
 outfile=$outdir$f
 cat $infile >> $outfile
done