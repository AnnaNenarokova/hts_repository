#!/bin/bash
#SBATCH --job-name=CE_lgg_filtered
#SBATCH --output=/scratch/nenarokova/code/slurm_out/CE_lgg_filtered_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=10G

fasta="/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/ce_filtered/concat/lgg/CE_81_markers_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 10