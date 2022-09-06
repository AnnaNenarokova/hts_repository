#!/bin/bash
#SBATCH --job-name=concat_AE_c60_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_AE_tree_testing_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

msa=""

iqtree2 -s $msa  -T AUTO --threads-max 48 -m MF -madd LG+C10,LG+C10+G,LG+C10+R,LG+C10+F,LG+C10+R+F,LG+C10+G+F,LG+C20,LG+C20+G,LG+C20+F,LG+C20+G+F,LG+C20+R,LG+C20+R+F --score-diff all
