#!/bin/bash

#SBATCH --job-name=iqtree_array
#SBATCH --partition=taw
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=14-00:0:0
#SBATCH --mem=100G
#SBATCH --array=1-11

cd /user/home/vl18625/code/ngs/projects/euk/
srun iqtree_array.sh
