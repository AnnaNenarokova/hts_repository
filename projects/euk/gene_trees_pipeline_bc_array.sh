#!/bin/bash

module load Java/1.8.0_92 apps/mafft/gnu/7.471-with-ext

bmge="/user/home/vl18625/tools/BMGE-1.12/BMGE.jar"
iqtree="/user/home/vl18625/tools/iqtree-1.6.12-Linux/bin/iqtree/"

fasta_dir="/user/work/vl18625/euk_ed_markers/fasta_euks_unaligned/"
msa_dir="/user/work/vl18625/euk_ed_markers/fasta_euks_unaligned/"
trimmed_msa_dir="/user/work/vl18625/euk_ed_markers/fasta_euks_unaligned/"
tree_dir="/user/work/vl18625/euk_ed_markers/trees/"
fasta=$(ls $fasta_dir*.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
trimmed_msa=$trimmed_msa_dir$fasta

mafft-linsi $fasta > $msa
java -jar $bmge -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa

cd tree_dir

$iqtree -s $f -m MFP -bb 1000 -nt AUTO