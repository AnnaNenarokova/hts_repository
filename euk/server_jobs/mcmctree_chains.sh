#!/bin/bash
#SBATCH --job-name=mcmctree
#SBATCH --output=/scratch/nenarokova/code/slurm_out/mcmctree_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=99-12:00:00
#SBATCH --array=1-4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=50GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/toyset_benoit/mcmctree/chain"${SLURM_ARRAY_TASK_ID}"/"

echo $workdir

control_file=$workdir"mcmctree.ctl"
bin_path="/scratch/nenarokova/tools/paml4.9i/src/"
PATH=$PATH:$bin_path

cd $workdir
mcmctree $control_file