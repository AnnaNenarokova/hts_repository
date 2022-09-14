#!/bin/bash
#SBATCH --job-name=concat_AE_c60_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_AE_tree_testing_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/model_testing_2/euk_65_markers_all_filtered_concat.fasta"

models="LG+C60,LG+C60+G,LG+C60+R,LG+C60+F,LG+C60+G+R,LG+C60+G+F,LG+C60+R+F,LG+C60+G+R+F,LG+PMSF+G"

iqtree2 -s $msa  -T AUTO --threads-max 48 -m MF -mset $models --score-diff all

