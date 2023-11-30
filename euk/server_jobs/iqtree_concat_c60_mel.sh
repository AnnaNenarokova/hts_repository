#!/bin/bash
#SBATCH --job-name=A_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/Archaea_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=261G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/archaea/concat/lgg_c60/archaea_85_markers_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 10 -T AUTO