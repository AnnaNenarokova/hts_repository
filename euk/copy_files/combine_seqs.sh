#!/bin/bash

outdir="/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_all/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/BacEuk_markers_28_filtered_faa/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/BE_c20_monobranch_sets_filtered_fastas/"
cd $outdir

for f in *.faa
do
 echo $f
 infile=$indir$f
 outfile=$outdir$f
 cat $infile >> $outfile
done