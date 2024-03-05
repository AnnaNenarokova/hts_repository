#!/bin/bash
#SBATCH --job-name=580_cyano
#SBATCH --output=/scratch/nenarokova/code/slurm_out/580_cyano_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=6G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_580_tips/05_03_24_alternative_topologies/alt_cyano/abce_94_markers_580_tips.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_580_tips/05_03_24_alternative_topologies/alt_cyano/alt_cyano_580.tree"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 10