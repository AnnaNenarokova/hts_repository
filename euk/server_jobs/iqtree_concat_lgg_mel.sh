#!/bin/bash
#SBATCH --job-name=euks_132_markers_concat_lgg_tree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/euks_132_markers_concat_lgg_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=30G

fasta="/scratch/nenarokova/euk/markers/abe/only_euks/euks_132_markers_concat/lgg/"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 48