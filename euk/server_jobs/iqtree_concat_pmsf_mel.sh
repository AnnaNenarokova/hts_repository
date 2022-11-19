#!/bin/bash
#SBATCH --job-name=euks_132_markers_concat_c60_lgg_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/euks_132_markers_concat_c60_lgg_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/only_euks/euks_132_markers_concat/c60_lgg_pmsf/only_euks_132_markers_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/only_euks/euks_132_markers_concat/lgg/lgg.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt 20
