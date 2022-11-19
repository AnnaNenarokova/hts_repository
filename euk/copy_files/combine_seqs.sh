#!/bin/bash

outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/alpha/brett_data/Set1/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/alpha/brett_data/Set1/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/alpha/brett_data/v3_D4993_C5/"

cd $outdir
for f in *.faa
do
 echo $f
 infile=$indir$f
 outfile=$outdir$f
 cat $infile >> $outfile
done