#!/bin/bash

outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/euk_largest_branches/fasta/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done