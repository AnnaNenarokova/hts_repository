#!/bin/bash
#SBATCH --job-name=concat_ae_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_ae_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=100G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/ae_set_concat/68_final/68_all_filtered_c60_pmsf/final_68ae_all_filtered_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/ae_set_concat/68_final/68_all_filtered_lgg/final_68ae_all_filtered_concat.fasta.treefile"
iqtree2 -s $msa -m LG+C60+F+G -ft $tree -b 1000 -nt 40