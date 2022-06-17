#!/bin/bash
#SBATCH --job-name=concat_be_alpha_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_be_alpha_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=100G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/be_alpha_40/concat/be_alpha_38_concat.faa"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/be_alpha_40/concat/be_alpha_38_concat.faa.treefile"
iqtree2 -s $msa -m LG+C60+F+G -ft $tree -b 1000 -nt 40