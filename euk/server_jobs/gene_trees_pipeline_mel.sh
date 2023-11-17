#!/bin/bash
#SBATCH --job-name=bact_sgt
#SBATCH --output=/scratch/nenarokova/code/slurm_out/bact_sgt_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=99-99:00:00
#SBATCH --array=1-115
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

workdir="/scratch/nenarokova/euk/markers/bacteria/all_bacteria_markers/"
fasta_dir=$workdir"faa/"

linsi_dir=$workdir"linsi/"
trimmed_linsi_dir=$workdir"linsi_bmge/"
tree_dir=$workdir"treefiles/"

cd $fasta_dir

fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$linsi_dir$fasta
trimmed_msa=$trimmed_linsi_dir$fasta
copy_trimmed_msa=$tree_dir$fasta

linsi --anysymbol $fasta > $msa
BMGE -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa

cp $trimmed_msa $copy_trimmed_msa
cd $tree_dir

iqtree2 -s $fasta -m LG+G -B 1000 -nt 1 -redo
