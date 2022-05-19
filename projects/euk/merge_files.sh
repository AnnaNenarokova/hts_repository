#!/bin/bash
dir1="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/final_ae_sets/final_ae_all_filtered/faa/"
dir2="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/arch_seqs_manual_cleaning/"

cd $dir1

for f in *.faa
do
	echo $f
	cat $dir2$f >> $dir1$f
done