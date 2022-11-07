#!/bin/bash
#SBATCH --job-name=94_abce_final_gene_trees
#SBATCH --output=/scratch/nenarokova/code/slurm_out/94_abce_final_gene_trees_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-94
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=5GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/markers/abe/abce_final_dataset/"

fasta_dir=$workdir"faa/"

linsi_dir=$workdir"linsi/"
trimmed_linsi_dir=$workdir"linsi_bmge/"

cd $fasta_dir

fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$linsi_dir$fasta
trimmed_msa=$trimmed_linsi_dir$fasta

linsi --anysymbol $fasta > $msa
BMGE -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa

cd $trimmed_linsi_dir

iqtree2 -s $fasta -m LG+G -B 1000 -nt 1 -redo
