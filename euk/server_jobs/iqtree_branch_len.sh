#!/bin/bash
#SBATCH --job-name=aebe_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/aebe_lengths_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/scratch/nenarokova/euk/markers/abe/one_hit/old_data/abce_94_markers_concat/only_length/aebe/c60/abce_94_markers_concat.fasta"
tree="/scratch/nenarokova/euk/markers/abe/one_hit/old_data/abce_94_markers_concat/only_length/aebe/c60/aebe_manual_sorted_ids_only.phy"
iqtree2 -s $msa -te $tree -m C60+LG+G -T AUTO --threads-max 20