#!/bin/bash
#SBATCH --job-name=pmsf_be_sgt
#SBATCH --output=/scratch/nenarokova/code/slurm_out/pmsf_be_sgt_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-115
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=5GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/markers/be/alpha/initial/"

msa_dir=$workdir"linsi_bmge/"
lgg_dir=$workdir"iqtree_lgg/"

cd $msa_dir
name=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $name
msa=$msa_dir$fasta
tree=$lgg_dir$name".treefile"

iqtree2 -s $msa -m LG+C20+F+G -ft $tree -B 1000 -nt 1
