#!/bin/bash
cog_dir="/Users/anna/work/euk_local/ed_markers/fastas_untrimmed/"

cd $cog_dir
for fasta in *.faa
do
  aligned=$fasta".aligned.fasta"
  linsi $fasta > $aligned
  hmm_file=$fasta".hmm"
  hmmbuild $hmm_file $aligned
done

