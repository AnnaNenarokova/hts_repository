#!/bin/bash
cog_dir="/Users/anna/work/euk_local/ed_markers/fastas_with_euks/"

cd $cog_dir
for fasta in *.faa
do
  aligned=$fasta".aligned"
  mafft $fasta > $aligned
  trimmed=$fasta".trimmed.fasta"
  bmge -i $aligned -t AA -m BLOSUM30 -o $trimmed
done
