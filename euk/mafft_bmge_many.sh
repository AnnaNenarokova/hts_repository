#!/bin/bash
unaligned_dir="/Users/anna/work/euk_local/ed_markers/fastas_with_euks/"
aligned_dir="/Users/anna/work/euk_local/ed_markers/fasta_euks_aligned/"
trimmed_dir="/Users/anna/work/euk_local/ed_markers/fasta_euks_al_trimmed/"

cd $unaligned_dir
for fasta in *.faa
do
  aligned=$aligned_dir$fasta".aligned"
  mafft-linsi $fasta > $aligned
  trimmed=$trimmed_dir$fasta
  bmge -i $aligned -t AA -m BLOSUM30 -o $trimmed
done
