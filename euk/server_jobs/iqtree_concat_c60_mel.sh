#!/bin/bash
#SBATCH --job-name=ae_no_meta_c60_lggf
#SBATCH --output=/scratch/nenarokova/code/slurm_out/ae_no_meta_c60_lggf_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=300G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/one_hit/ae_81_markers_11_03_24_all/ae_no_meta_81_markers_11_03_24/concat/c60_lggf/ae_81_markers_no_meta.fasta"
iqtree2 -s $fasta -m LG+C60+G+F -mwopt -B 1000 --threads-max 10 -T AUTO