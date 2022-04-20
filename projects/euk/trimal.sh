#!/bin/bash
trimal="/Users/vl18625/work/tools/trimAl/source/trimal"

al_dir="/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/msa1_linsi_bmge/"
cleaned_dir="/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/msa1_linsi_bmge_trimal_50/"
mkdir $cleaned_dir
cd $al_dir

for msa in *.faa
do
    cleaned_msa=$cleaned_dir$msa
    echo $msa
    $trimal -in $msa -out $cleaned_msa -resoverlap 0.50 -seqoverlap 50
done
