#!/bin/bash
#SBATCH --job-name=94ab_c60_no_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/94ab_c60_no_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ab/ab_94markers/no_idunn_concat/c60_lgg/ab_94_markers_no_idunn_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 48 -T AUTO