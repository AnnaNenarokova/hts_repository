#!/bin/bash
#SBATCH --job-name=recoded_abce_94_markers
#SBATCH --output=/scratch/nenarokova/code/slurm_out/recoded_abce_94_markers_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

msa=""

iqtree2 -s $fasta -m GTR+G -B 1000 -T AUTO --threads-max 48