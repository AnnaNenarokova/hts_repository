#!/bin/bash
#SBATCH --job-name=104sp_no_pmsf_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/104sp_no_pmsf_c60_%A.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94m_104_species_concat/c60_no_pmsf/104species_94markers_abce.fasta"
iqtree2 -s $fasta -m LG+C60+G -B 1000 --threads-max 48 -T AUTO