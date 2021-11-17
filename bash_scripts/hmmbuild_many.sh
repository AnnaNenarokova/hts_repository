#!/bin/bash
cog_dir="/Users/anna/work/euk_local/ed_markers_trimmed/"

cd $cog_dir
for fasta in *.fas
do
    hmm_file=$fasta".hmm"
    hmmbuild $hmm_file $fasta
done
