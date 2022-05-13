#!/bin/bash
#SBATCH --job-name=concat_ae_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_ae_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=100G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/nina_markers/ae_sets_only_euks/iqtree_linsi_bmge_trimal75_concatenated/ae_only_euk_linsi_bmge_trimal_75_concatenated.faa"
iqtree2 -s $fasta -m LG+G+F -B 1000 -nt 40