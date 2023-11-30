#!/bin/bash
#SBATCH --job-name=c30_Bacteria
#SBATCH --output=/scratch/nenarokova/code/slurm_out/c30_Bacteria_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/bacteria/all_bacteria_markers/concat/c30_lgg/bacteria_115_markers_concat.fasta"
iqtree2 -s $fasta -m LG+C30+G -B 1000 --threads-max 10 -T AUTO