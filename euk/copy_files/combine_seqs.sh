#!/bin/bash

outdir="/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_all/"
for f in *.faa
do
<<<<<<< HEAD
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/euk_only_fastas/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/be_alpha_28/"
for f in *.faa
do
 echo $f
 infile=$indir$f
 outfile=$outdir$f
 cat $infile >> $outfile
=======
 echo $f
 outfile=$outdir$f
 cat $f >> $outfile
>>>>>>> d332b1b8576d7c006cd73c2a738af8f8b3d2ea5b
done