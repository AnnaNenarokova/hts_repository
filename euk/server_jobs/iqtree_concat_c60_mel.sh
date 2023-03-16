#!/bin/bash
#SBATCH --job-name=68ae_c60_no_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/68ae_c60_no_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/final_68ae_filtered_concat/lgg_c60/68_final_ae.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 48 -T AUTO