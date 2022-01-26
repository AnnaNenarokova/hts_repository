#!/bin/bash

module load apps/bmge/1.12 apps/iqtree/1.6.12 apps/mafft/7.429

bmge="/sw/apps/BMGE-1.12/BMGE.jar"

fasta_dir="/user/home/vl18625/euk/ed_markers/unaligned/"
msa_dir="/user/home/vl18625/euk/ed_markers/aligned/"
trimmed_msa_dir="/user/home/vl18625/euk/ed_markers/aligned_trimmed/"
tree_dir="/user/home/vl18625/euk/ed_markers/trees/"

mkdir $msa_dir
mkdir $trimmed_msa_dir
mkdir $tree_dir

cd $fasta_dir
fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
trimmed_msa=$trimmed_msa_dir$fasta

mafft-linsi $fasta > $msa
java -jar $bmge -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa

cd $tree_dir

iqtree -s $f -m MFP -bb 1000 -nt AUTOp