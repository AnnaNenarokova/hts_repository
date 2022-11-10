#!/bin/bash
#SBATCH --job-name=concat_lgg_abce_94_markers_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/concat_lgg_abce_94_markers_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=15G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/abce_94_markers_concat.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 48