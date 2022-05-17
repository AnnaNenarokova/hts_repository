#!/bin/bash
#SBATCH --job-name=final_ae_gene_trees
#SBATCH --output=/scratch/nenarokova/code/slurm_out/be_alpha_gene_treesp_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-115
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=6GB
##SBATCH --nodes=1
## --cpu_bind=v,threads


outdir="/scratch/nenarokova/euk/markers/be_mono_results/alpha/"

fasta_dir=$outdir"faa/"
msa_dir=$outdir"msa/"
trimmed_msa_dir=$outdir"msa_bmge/"

linsi_dir=$outdir"linsi/"
trimmed_linsi_dir=$outdir"linsi_bmge/"
cd $fasta_dir

fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
trimmed_msa=$trimmed_msa_dir$fasta

mafft --anysymbol $fasta > $msa
BMGE -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa

msa=$linsi_dir$fasta
trimmed_msa=$trimmed_linsi_dir$fasta

linsi --anysymbol $fasta > $msa
BMGE -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa

cd $trimmed_linsi_dir

iqtree2 -s $fasta -m LG+G -B 1000 -nt 1 
