#!/bin/bash
#SBATCH --job-name=concat_BE_alpha_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_BE_tree_c60_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/concat/c20_initial_58/c60_pmsf_lgg/be_c20_filtered_58_markers_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/concat/c20_initial_58/lgg/be_c20_filtered_58_markers_concat.fasta.treefile"
iqtree2 -s $msa -m LG+C60+F+G -ft $tree -b 1000 -nt 40