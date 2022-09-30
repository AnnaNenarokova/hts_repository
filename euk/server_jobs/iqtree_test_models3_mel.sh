#!/bin/bash
#SBATCH --job-name=AE_model_test
#SBATCH --output=/scratch/nenarokova/code/slurm_out/AE_model_test_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/model_testing/model_testing_6/euk_65_markers_all_filtered_concat.fasta"
models="LG+C60+R2,LG+C60+R2+F,LG+C60+R3,LG+C60+R3+F,LG+C60+G4,LG+C60+G6,LG+C60+G8"

iqtree2 -s $msa -T 8 -m MF -mset $models --score-diff all -mem 250G

