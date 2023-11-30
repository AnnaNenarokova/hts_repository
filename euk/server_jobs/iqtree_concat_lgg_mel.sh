#!/bin/bash
#SBATCH --job-name=CE_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/CE_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=10G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/cyano/concat/lgg/CE_102_markers_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 10