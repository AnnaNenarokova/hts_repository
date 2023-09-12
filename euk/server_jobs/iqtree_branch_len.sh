#!/bin/bash
#SBATCH --job-name=branch_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/branch_lengths_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=150G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/one_hit/old_data/only_euks/117euks_132markers_concat/c60_lgg_only_len/117euks_132markers_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/one_hit/old_data/only_euks/117euks_132markers_concat/c60_lgg_only_len/only_euks_manual_only_ids.tree"
iqtree2 -s $msa -te $tree -m C60+LG+G -T AUTO --threads-max 20