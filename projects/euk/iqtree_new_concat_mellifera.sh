#!/bin/bash
#SBATCH --job-name=concat_ae_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_ae_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=20G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/archaea/ae_set_concat/65_markers_filtered_LG_G/ae_65_markers_concat.fasta"
iqtree2 -s $fasta -m LG+G -nt 20