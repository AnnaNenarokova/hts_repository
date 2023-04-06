#!/bin/bash
#SBATCH --job-name=au_test_68_ae_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/au_test_68_ae_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=99-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=50G

msa="/scratch/nenarokova/euk/markers/ae/one_hit/final_68ae_filtered_concat/au_tests_constraint_hemidall/lgg_20000/68_final_ae.fasta"
trees_file="/scratch/nenarokova/euk/markers/ae/one_hit/final_68ae_filtered_concat/au_tests_constraint_hemidall/lgg_20000/68_final_ae.trees"
iqtree2 -s $msa -m LG+G -z $trees_file -T 10 -n 0 -zb 20000 -au