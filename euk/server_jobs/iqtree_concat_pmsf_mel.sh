#!/bin/bash
#SBATCH --job-name=abce_c60_lgg_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/abce_c60_lgg_pmsf_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/c60_pmsf/abce_94_markers_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/lgg/abce_94_markers_concat.fasta.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt 20
