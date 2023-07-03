#!/bin/bash
#SBATCH --job-name=codeML
#SBATCH --output=/scratch/nenarokova/code/slurm_out/codeML_%A.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50G

workdir="/mnt/alvarium2pool/scratch/nenarokova/euk/toyset_benoit/mcmctree_method1/"
control_file="/mnt/alvarium2pool/scratch/nenarokova/euk/toyset_benoit/mcmctree_method1/tmp0001.ctl"
bin_path="/scratch/nenarokova/tools/paml4.9i/src/"
PATH=$PATH:$bin_path

cd $workdir

codeml $control_file