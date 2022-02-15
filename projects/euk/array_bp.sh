#!/bin/bash

#SBATCH --job-name=iqtree_array
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --time=14-00:0:0
#SBATCH --mem=1000M
#SBATCH --array=1-5

cd /user/home/vl18625/code/ngs/projects/euk/
srun gene_trees_pipeline_bp_array.sh
