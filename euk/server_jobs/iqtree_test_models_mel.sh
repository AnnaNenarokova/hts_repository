#!/bin/bash
#SBATCH --job-name=model_test_ABE_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/model_test_ABE_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=500G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94_markers_concat/model_testing/abce_94_markers_concat.fasta"
models="LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C50+G,LG+C60+G"

iqtree2 -s $msa -T 20 -m MF -madd $models --score-diff all
