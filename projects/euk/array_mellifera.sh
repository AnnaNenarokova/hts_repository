#!/bin/bash
#SBATCH --job-name=ae_markers
#SBATCH --output=ae_markers_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-87
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=6GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

cd /scratch/nenarokova/code/ngs/projects/euk/

srun gene_trees_pipeline_mellifera.sh