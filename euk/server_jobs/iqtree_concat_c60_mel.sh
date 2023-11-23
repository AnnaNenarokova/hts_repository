#!/bin/bash
#SBATCH --job-name=c60_Bacteria
#SBATCH --output=/scratch/nenarokova/code/slurm_out/c60_Bacteria_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/bacteria/all_bacteria_markers/concat/c60_lgg/bacteria_115_markers_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 20 -T AUTO