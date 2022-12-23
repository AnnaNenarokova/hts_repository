#!/bin/bash
#SBATCH --job-name=brett_16_markers_lgg_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/brett_16_markers_lgg_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=85G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/brett_16markers/concat_16_markers/no_anaerobs/lgg_c60_pmsf/16_markers_brett_concat_no_anaerobs.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/brett_16markers/concat_16_markers/no_anaerobs/lgg/16_markers_brett_concat_no_anaerobs.fasta.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt 20
