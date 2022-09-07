#!/bin/bash
#SBATCH --job-name=concat_AE_c60_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_AE_tree_testing_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/c60_lg_f_g_pmsf/euk_65_markers_all_filtered_concat.fasta"

models="LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C50+G,LG+C60+G"

iqtree2 -s $msa  -T AUTO --threads-max 48 -m MF -madd $models --score-diff all
