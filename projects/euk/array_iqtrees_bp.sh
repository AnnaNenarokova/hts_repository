#!/bin/bash

#SBATCH --job-name=iqtree
#SBATCH --partition=taw
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:0:0
#SBATCH --mem=20G
#SBATCH --array=1-25

cd /user/home/vl18625/code/ngs/projects/euk/
srun iqtree_MFP_array.sh
