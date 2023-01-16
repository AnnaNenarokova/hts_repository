#!/bin/bash
#SBATCH --job-name=recoded_abce_94_markers_gtr_g
#SBATCH --output=/scratch/nenarokova/code/slurm_out/recoded_abce_94_markers_gtr_g_%A.out
#SBATCH --partition=high
#SBATCH --time=99-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/recoded_msa/dayhoff4/gtr_g/abce_94_markers_16_01_dayhoff4_recoded.fasta"

iqtree2 -s $msa -m GTR+G -B 1000 -T AUTO --threads-max 48