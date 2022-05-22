#!/bin/bash
#SBATCH --job-name=concat_ae_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_ae_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=10G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/ae_set_concat/68_all_filtered_trimal85_LG_G/final_68ae_all_filtered_trimal85_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -nt 40