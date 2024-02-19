#!/bin/bash
#SBATCH --job-name=alt_tack_euk_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/alt_tack_euk_len_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=15G
msa="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_1211_tips/alt_topologies_19_02_24/tack_euk_alt/abce_94_markers_concat_filtered.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_1211_tips/alt_topologies_19_02_24/tack_euk_alt/abce_alt_tack_euk.tree"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 10