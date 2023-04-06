#!/bin/bash

#SBATCH --job-name=mafft_array
#SBATCH --partition=taw
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:0:0
#SBATCH --mem=10G
#SBATCH --array=1-5

cd /user/home/vl18625/code/ngs/projects/euk/
srun mafft_bmge_bp_array.sh