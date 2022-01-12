#!/bin/bash

module load mafft iqtree-2.1.0 BMGE-1.12

outdir="/home/users/nenarokova/euk/cogs_with_euks/"
bmge="/home/software/BMGE-1.12/BMGE.jar"

fasta_dir=$outdir"fasta/"
msa_dir=$outdir"msa/"
trimmed_msa_dir=$outdir"trimmed_msa/"
iqtree_dir=$outdir"iqtree_files/"
tree_dir=$outdir"trees"

cd $fasta_dir

fasta=$(ls *.fa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta".aligned.fasta"
trimmed_msa=$trimmed_msa_dir$fasta"_trimmed_msa.fasta"
mafft --localpair --maxiterate 1000 --inputorder --thread -1 $fasta > $msa
java -jar $bmge -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa
iqtree2 -s $trimmed_msa -m MFP -bb 1000 -nt AUTO
