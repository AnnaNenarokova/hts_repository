#!/bin/bash

module load mafft iqtree-2.1.0

outdir="/home/users/nenarokova/euk/cogs_with_euks/"
bmge="/home/users/nenarokova/tools/BMGE-1.12/BMGE.jar"

# creating directories
fasta_dir=$outdir"fasta/"

msa_dir=$outdir"msa/"
trimmed_msa_dir=$outdir"trimmed_msa/"
iqtree_dir=$outdir"iqtree_files/"
tree_dir=$outdir"trees"

rm -r $msa_dir
mkdir $msa_dir
rm -r $trimmed_msa_dir
mkdir $trimmed_msa_dir
rm -r $iqtree_dir
mkdir $iqtree_dir
rm -r $tree_dir
mkdir $tree_dir

cd $fasta_dir

fasta=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta".aligned.fasta"
trimmed_msa=$trimmed_msa_dir$fasta"_trimmed_msa.fasta"
linsi --inputorder $fasta > $msa
java -jar $bmge -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa
iqtree2 $iqtree -s $f -m MFP -bb 1000 -nt 1
