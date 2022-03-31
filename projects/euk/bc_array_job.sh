#!/bin/bash
#SBATCH --job-name=busco_array
#SBATCH --partition=serial
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:0:0
#SBATCH --mem=1000M
#SBATCH --array=1-726

cd /user/home/vl18625/code/ngs/projects/euk/

srun busco_bc_array.sh