#!/bin/bash
#SBATCH --job-name=aebe_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/aebe_lengths_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/one_hit/old_data/abce_94_markers_concat/only_length/aebe/lgg4f_14_11/aebe_110_euks_94_markers_concat_filtered.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/one_hit/old_data/abce_94_markers_concat/only_length/aebe/lgg4f_14_11/aebe_manual_only_ids_no_alpha_metamonads.phy"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 20