#!/bin/bash
#SBATCH --job-name=CE_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/CE_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=100G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/ce_filtered/concat/c60_lgg/CE_81_markers_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 10 -T AUTO