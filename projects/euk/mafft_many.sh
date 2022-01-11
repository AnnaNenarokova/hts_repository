#!/bin/bash
cog_dir="/Users/anna/work/euk_local/cogs_arcogs/arCOGs/arcogs_nina_set/fasta_M_filtered/"

cd $cog_dir
for fasta in *.fa
do
  aligned=$fasta".aligned.fasta"
  mafft $fasta > $aligned
done

