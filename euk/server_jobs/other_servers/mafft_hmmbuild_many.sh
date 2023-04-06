#!/bin/bash
infasta_dir="/Users/anna/work/euk_local/ed/ed_markers/fasta_filtered/"
aligned_dir="/Users/anna/work/euk_local/ed/ed_markers/fasta_filt_aligned/"
hmm_dir="/Users/anna/work/euk_local/ed/ed_markers/hmm_filtered/"
cd $infasta_dir
for fasta in *.faa
do
  aligned_file=$aligned_dir$fasta".aligned.fasta"
  mafft $fasta > $aligned_file
  hmm_file=$hmm_dir$fasta".hmm"
  hmmbuild $hmm_file $aligned_file
done

