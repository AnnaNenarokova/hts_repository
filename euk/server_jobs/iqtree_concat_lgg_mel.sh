#!/bin/bash
#SBATCH --job-name=68_final_ae_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/68_final_ae_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=50G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/final_68ae_filtered_concat/lgg/68_final_ae.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20