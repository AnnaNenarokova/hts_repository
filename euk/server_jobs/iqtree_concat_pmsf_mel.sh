#!/bin/bash
#SBATCH --job-name=ae_non_asgard_c60_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/ae_non_asgard_c60_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=150G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/only_non_asgard/c60_lgg_pmsf/34_ae_non_asgard_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/only_non_asgard/lgg/34_ae_non_asgard_concat.fasta.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt 20
