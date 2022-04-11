#!/bin/bash
trimal="/Users/vl18625/work/tools/trimAl/source/trimal"

al_dir="/Users/vl18625/work/euk/markers_euks/ed_markers/mono_msa_trimmed/"
cleaned_dir="/Users/vl18625/work/euk/markers_euks/ed_markers/mono_msa_bmge_trimal_75/"
mkdir $cleaned_dir
cd $al_dir

for msa in *.faa
do
    cleaned_msa=$cleaned_dir$msa
    echo $msa
    $trimal -in $msa -out $cleaned_msa -resoverlap 0.75 -seqoverlap 75
done
