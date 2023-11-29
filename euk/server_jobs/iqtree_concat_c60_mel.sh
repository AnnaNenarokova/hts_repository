#!/bin/bash
#SBATCH --job-name=CE_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/c60_CE_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/cyano/concat/lgg_c60/CE_102_markers_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 20 -T AUTO