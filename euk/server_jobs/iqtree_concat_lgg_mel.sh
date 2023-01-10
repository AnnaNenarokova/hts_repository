#!/bin/bash
#SBATCH --job-name=34_ae_non_asgard_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/34_ae_non_asgard_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=20G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/only_non_asgard/lgg/34_ae_non_asgard_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20