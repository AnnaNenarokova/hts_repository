#!/bin/bash
#SBATCH --job-name=baldauf_580
#SBATCH --output=/scratch/nenarokova/code/slurm_out/baldauf_580_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=6G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_580_tips/05_03_24_alternative_topologies/alt_baldauf/abce_94_markers_580_tips.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_580_tips/05_03_24_alternative_topologies/alt_baldauf/alt_baldauf_580.tree"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 10