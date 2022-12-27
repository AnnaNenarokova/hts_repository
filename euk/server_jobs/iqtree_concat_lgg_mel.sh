#!/bin/bash
#SBATCH --job-name=34_ae_asgard_only_lgg_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/34_ae_asgard_only_lgg_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=30G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/only_asgard/34_ae_asgard_concat/lgg/34_ae_asgard_only_concat.faa"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20