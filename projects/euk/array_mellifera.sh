#!/bin/bash
#SBATCH --job-name=hmmsearch
#SBATCH --output=hmmsearch_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-87
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=6GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

cd /scratch/nenarokova/code/ngs/projects/euk/

srun mafft_hmmsearch_mellifera.sh