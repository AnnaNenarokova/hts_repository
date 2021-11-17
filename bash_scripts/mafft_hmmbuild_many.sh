#!/bin/bash
cog_dir="/Users/anna/work/euk_local/ed_markers_untrimmed/"

cd $cog_dir
for fasta in *.faa
do
  aligned=$fasta".aligned.fasta"
  mafft $fasta > $aligned
  hmm_file=$fasta".hmm"
  hmmbuild $hmm_file $aligned
done

