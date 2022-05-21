#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:0:0
#SBATCH --mem=1000M
#SBATCH --array=1-172

srun gene_trees_pipeline_bc_array.sh
