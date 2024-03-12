#!/bin/bash
#SBATCH --job-name=ae_lgg_no_meta
#SBATCH --output=/scratch/nenarokova/code/slurm_out/ae_lgg_no_meta_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=5G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/one_hit/ae_81_markers_11_03_24_all/ae_81_markers_11_03_24/concat/lgg/ae_81_markers.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 10