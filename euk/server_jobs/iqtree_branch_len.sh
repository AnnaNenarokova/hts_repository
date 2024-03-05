#!/bin/bash
#SBATCH --job-name=frank_580
#SBATCH --output=/scratch/nenarokova/code/slurm_out/frank_580_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=10G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_580_tips/05_03_24_alternative_topologies/frank/abce_94_markers_580_tips.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/molecular_clock_datasets/aebece_580_tips/05_03_24_alternative_topologies/frank/frank_580.tree"
iqtree2 -s $msa -te $tree -m LG+F+G4 -T AUTO --threads-max 10