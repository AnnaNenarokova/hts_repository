#!/bin/bash
#SBATCH --job-name=16_markers_brett_concat
#SBATCH --output=/scratch/nenarokova/code/slurm_out/16_markers_brett_concat_lgg_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=30G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/brett_16markers/concat_16_markers/no_anaerobs/lgg/16_markers_brett_concat_no_anaerobs.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20