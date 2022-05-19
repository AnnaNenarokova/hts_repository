#!/bin/bash
#SBATCH --job-name=concat_ae_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_ae_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/archaea/ae_set_concat/65_markers_filtered_LG_C60_PMSF/ae_65_markers_concat.fasta"
lg_tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/archaea/ae_set_concat/65_markers_filtered_LG_G/ae_65_markers_concat.fasta.treefile"

iqtree2 -s $msa -m LG+C60+F+G -ft lg_tree -B 1000 -nt 40