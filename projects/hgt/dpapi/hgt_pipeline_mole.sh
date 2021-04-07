#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40
#SBATCH -N 1

module load mafft iqtree-2.1.0
threads="40"

outdir="/home/users/nenarokova/diplonema/hgt_new/"

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

for fasta in *.faa
do
    msa=$msa_dir$fasta".aligned.fasta"
    trimmed_msa=$trimmed_msa_dir$fasta"_trimmed_msa.fasta"
    mafft --auto --inputorder $fasta > $msa
    java -jar $bmge -i $msa -t "AA" -of $trimmed_msa
    iqtree2 -s $trimmed_msa -nt $threads -m LG+G+F -bb 1000 -bnni
done

