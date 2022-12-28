#!/bin/bash
#SBATCH --job-name=34_ae_asgard_only_c60_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/34_ae_asgard_only_c60_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=112G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/only_asgard/34_ae_asgard_concat/c60_pmsf/34_ae_asgard_only_concat.faa"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/only_asgard/34_ae_asgard_concat/lgg/34_ae_asgard_only_concat.faa.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt 20
