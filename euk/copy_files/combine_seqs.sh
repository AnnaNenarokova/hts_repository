#!/bin/bash

outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/abe/abc_dataset/abc_euks_fasta/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/nina_all_seqs/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/abc_dataset/abc_euks_fasta/"

for f in *.faa
do
 echo $f
 infile=$indir$f
 outfile=$outdir$f
 cat $infile >> $outfile
done