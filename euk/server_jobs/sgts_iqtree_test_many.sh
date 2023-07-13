#!/bin/bash
#SBATCH --job-name=ce_sgts_test_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/ce_sgts_test_c60_%A_%a.out
#SBATCH --partition=low
#SBATCH --time=99-99:00:00
#SBATCH --array=1-102
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/cyano/linsi_bmge/"
models="LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C50+G,LG+C60+G"

cd $workdir

msa=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

iqtree2 -s $msa -m MFP -madd $models --score-diff all
