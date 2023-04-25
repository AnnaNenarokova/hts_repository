#!/bin/bash
#SBATCH --job-name=branch_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/branch_lengths_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=50G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/toyset_benoit/short_names_2cyanos.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/toyset_benoit/short_names_tree_2cyanos_calibrated.tree"
iqtree2 -s $msa -te $tree -m C60+LG+G -T AUTO --threads-max 20