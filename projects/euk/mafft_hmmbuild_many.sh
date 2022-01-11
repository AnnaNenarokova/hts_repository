#!/bin/bash
infasta_dir="/Users/anna/work/euk_local/cogs_arcogs/COGs/fasta_filtered/"
aligned_dir="/Users/anna/work/euk_local/cogs_arcogs/COGs/filtered_aligned/"
hmm_dir="/Users/anna/work/euk_local/cogs_arcogs/COGs/hmm_filtered_cogs/"
cd $infasta_dir
for fasta in *.fa
do
  aligned_file=$aligned_dir$fasta".aligned.fasta"
  mafft --anysymbol $fasta > $aligned_file
  hmm_file=$hmm_dir$fasta".hmm"
  hmmbuild $hmm_file $aligned_file
done

