#!/bin/bash
#SBATCH --job-name=fasta
#SBATCH --partition=high
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=20G


cd /scratch/nenarokova/code/ngs/projects/euk/

python3 prepare_hmm_hit_fastas.py