#!/bin/bash
#SBATCH --job-name=AE_fastas
#SBATCH --partition=high
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=50G
#SBATCH --output=/scratch/nenarokova/code/slurm_out/AE_fastas_%A_%a.out

cd /scratch/nenarokova/code/ngs/euk/hmm_results_scripts

python3 prepare_hmm_hit_fastas.py