#!/bin/bash
#SBATCH --job-name=104sp_abe_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/104sp_abe_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=10G

fasta="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/abe/abce_94m_104_species_concat/lgg/104species_94markers_abce.fasta"
iqtree2 -s $fasta -m LG+G -B 1000 -T AUTO --threads-max 20