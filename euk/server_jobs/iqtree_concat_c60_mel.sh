#!/bin/bash
#SBATCH --job-name=only_euks_132_markers_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/only_euks_132_markers_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/only_euks/euks_132_markers_concat/c60_lgg_no_pmsf/only_euks_132_markers_concat.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 48 -T AUTO