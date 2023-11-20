#!/bin/bash
#SBATCH --job-name=B_sgt_mtest
#SBATCH --output=/scratch/nenarokova/code/slurm_out/B_sgt_mtest_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --array=1-115
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/markers/bacteria/all_bacteria_markers/"

msa_dir=$workdir"linsi_bmge/"
tree_dir=$workdir"model_test/"

cd $msa_dir
name=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $name
msa=$msa_dir$name
msa_copy=$tree_dir$name

cp $msa $msa_copy

models="LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C50+G,LG+C60+G"

iqtree2 -s $msa_copy -B 1000 -nt 1 -m MFP -madd $models --score-diff all
