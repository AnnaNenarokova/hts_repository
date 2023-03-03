#!/bin/bash
#SBATCH --job-name=pmsf_abe_100sp
#SBATCH --output=/scratch/nenarokova/code/slurm_out/pmsf_abe_100sp_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=150G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94m_104_species_concat/c60_lgg_pmsf/104species_94markers_abce.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94m_104_species_concat/lgg/104species_94markers_abce.fasta.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt 20
