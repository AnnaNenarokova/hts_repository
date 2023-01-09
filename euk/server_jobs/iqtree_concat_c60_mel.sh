#!/bin/bash
#SBATCH --job-name=65_ae_no_pmsf_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/65_ae_no_pmsf_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/65_ae_markers_concat_23_08_22/c60_lgg/euk_65_markers_all_filtered_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 48 -T AUTO