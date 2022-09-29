#!/bin/bash

outdir="/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_all/"
for f in *.faa
do
	echo $f
	outfile=$outdir$f
	cat $f >> $outfile
done

<<<<<<< HEAD
indir="/Users/anna/work/euk_local/nina_markers/fasta_markers/bacteria_manually_cleaned/"
outdir="/Users/anna/work/euk_local/nina_markers/singlehit_results/alpha/be/28_markers_29_09_22/be_alpha_fastas/"
=======
indir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/BacEuk_markers_28_filtered_faa/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/BE_c20_monobranch_sets_filtered_fastas/"
cd $outdir

>>>>>>> 83c3850da30e76c2bdfaee6052b6bf9b2723a1c5
for f in *.faa
do
 echo $f
 infile=$indir$f
 outfile=$outdir$f
 cat $infile >> $outfile
done