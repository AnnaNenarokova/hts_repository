#!/bin/bash

outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/euk_alpha_fastas/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done