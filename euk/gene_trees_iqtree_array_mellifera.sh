#!/bin/bash
#SBATCH --job-name=final_ae_gene_trees
#SBATCH --output=/scratch/nenarokova/code/slurm_out/euk_trimal_gene_trees_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-70
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=6GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

trimmed_msa_dir="/scratch/nenarokova/euk/markers/nina_markers/ae_sets_only_euks/linsi_bmge_trimal_75/"

cd $trimmed_msa_dir

fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

iqtree2 -s $fasta -m LG+G -B 1000 -nt 1 
