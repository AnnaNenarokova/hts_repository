#!/bin/bash

folder="/user/work/vl18625/euk/ed_markers/anna_set_results/monobranch_linsi/faa_cleaned/cleaned_fastas/"

cd $folder

cog_folder="/user/work/vl18625/euk/ed_markers/faa_filtered/"

for f in *.faa
do 
	echo $f
	cat $cog_folder$f >> $f
done