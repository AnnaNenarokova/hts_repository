#!/bin/bash
#SBATCH --job-name=frank_bfixed
#SBATCH --output=/scratch/nenarokova/code/slurm_out/frank_bfixed_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=15G
msa="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_1211_tips/22_02_2024/frankenstein/abce_94_markers_concat_filtered.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_1211_tips/22_02_2024/frankenstein/fixed_bacteria_frankenstein.tree"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 10