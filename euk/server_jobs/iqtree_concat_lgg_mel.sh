#!/bin/bash
#SBATCH --job-name=ABaE_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/ABaE_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=50G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abAe/87_markers_concat/lgg/87_markers_filtered_ABaE_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20