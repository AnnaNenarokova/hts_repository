#!/bin/bash
#SBATCH --job-name=aebe_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/aebe_lengths_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/one_hit/old_data/abce_94_markers_concat/only_length/aebe/c60/aebe_110_euks_94_markers_concat_filtered.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/one_hit/old_data/abce_94_markers_concat/only_length/aebe/c60/aebe_manual_ids_only_edited.tree"
iqtree2 -s $msa -te $tree -m C60+LG+G -T AUTO --threads-max 20