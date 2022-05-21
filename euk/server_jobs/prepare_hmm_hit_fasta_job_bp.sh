#!/bin/bash
#SBATCH --job-name=fas_compute
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=20G

module load lang/python/anaconda/3.7-2019.03.biopython

cd /user/home/vl18625/code/ngs/projects/euk/

python3 prepare_hmm_hit_fastas.py