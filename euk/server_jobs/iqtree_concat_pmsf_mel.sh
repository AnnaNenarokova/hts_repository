#!/bin/bash
#SBATCH --job-name=c60_lgg_20t_AE_pmsf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/c60_lgg_20t_pmsf_AE_concat_tree_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=250G

msa="/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/c60_lgg_pmsf/euk_65_markers_all_filtered_concat.fasta"
tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_euk_filtered_23_08_22/lgg/euk_65_markers_all_filtered_concat.fasta.treefile"
iqtree2 -s $msa -m LG+C60+G -ft $tree -B 1000 -nt AUTO -ntmax 20
