#!/bin/bash
#SBATCH --job-name=concat_AE_c60_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_AE_tree_c60_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/c60_lg_f_g_pmsf/euk_65_markers_all_filtered_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/lgg/euk_65_markers_all_filtered_concat.fasta.treefile"
iqtree2 -s $msa -m LG+C60+F+G -ft $tree -b 1000 -T AUTO --threads-max 48
