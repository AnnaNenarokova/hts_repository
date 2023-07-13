#!/bin/bash
#SBATCH --job-name=be_sgts_test_c60
#SBATCH --output=/scratch/nenarokova/code/slurm_out/be_sgts_test_c60_%A_%a.out
#SBATCH --partition=low
#SBATCH --time=99-99:00:00
#SBATCH --array=1-119
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/alpha/linsi_bmge/"
msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/be/alpha/brett_16markers/concat_16_markers/model_testing/16_markers_brett_concat.fasta"
models="LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C50+G,LG+C60+G"

cd $workdir

msa=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

iqtree2 -s $msa -m MFP -madd $models --score-diff all
