#!/bin/bash
#SBATCH --job-name=concat_BE_filtered_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_be_filtered_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=10G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/concat/be_c20_filtered_58_markers_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -nt 40