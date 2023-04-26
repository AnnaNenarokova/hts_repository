#!/bin/bash
#SBATCH --job-name=mcmctree2
#SBATCH --output=/scratch/nenarokova/code/slurm_out/mcmctree2_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50G

workdir="/scratch/nenarokova/euk/toyset_benoit/mcmctree_phylip"

control_file=$workdir"mcmctree.ctl"
bin_path="/scratch/nenarokova/tools/paml4.9i/src/"
PATH=$PATH:$bin_path

cd $workdir
mcmctree $control_file