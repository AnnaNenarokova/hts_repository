#!/bin/bash
#SBATCH --job-name=abce_94_no_kor_c30_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/abce_94_no_kor_c30_pmsf_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/filtered/lgg_c30_pmsf/abce_94_markers_no_kor_filtered.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/filtered/lgg/abce_94_markers_no_kor_filtered.fasta.treefile"
iqtree2 -s $msa -m LG+C30+G -ft $tree -B 1000 -nt 20
