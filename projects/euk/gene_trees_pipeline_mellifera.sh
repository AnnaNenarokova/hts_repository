#!/bin/bash

outdir="/scratch/nenarokova/euk/nina_markers/euk_largest_monobranch/arch/"

fasta_dir=$outdir"fasta/"
msa_dir=$outdir"msa_linsi/"
trimmed_msa_dir=$outdir"msa_linsi_bmge/"

cd $fasta_dir

fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
trimmed_msa=$trimmed_msa_dir$fasta
linsi --anysymbol $fasta > $msa
BMGE -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa
cd $trimmed_msa_dir

iqtree2 -s $fasta -m LG+G -B 1000 -nt 1 
