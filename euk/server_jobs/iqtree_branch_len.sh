#!/bin/bash
#SBATCH --job-name=aebece_lengths
#SBATCH --output=/scratch/nenarokova/code/slurm_out/aebece_lengths_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=15G
msa="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_1211_tips/lgg4f_29_01_24/abce_94_markers_concat_filtered.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_1211_tips/lgg4f_29_01_24/ABAEBECE_manual_only_ids_no_tabs_29_01_24.nwk.phy"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 10