#!/bin/bash
#SBATCH --job-name=abce_94_markers_no_kor_lgg_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/abce_94_markers_no_kor_lgg_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=50G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/filtered/lgg/abce_94_markers_no_kor_filtered.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20