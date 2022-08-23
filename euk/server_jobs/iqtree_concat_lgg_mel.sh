#!/bin/bash
#SBATCH --job-name=concat_be_alpha_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_ae_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=10G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/euk_65_markers_all_filtered_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -nt 20