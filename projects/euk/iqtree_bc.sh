#!/bin/bash
#SBATCH --job-name=iqtree_cogs
#SBATCH --partition=cpu*
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#SBATCH --time=14-00:00:00
#SBATCH --mem=100M

threads=28

workdir="/mnt/storage/scratch/vl18625/ed_cogs_with_euks/"
iqtree="/mnt/storage/home/vl18625/tools/iqtree-1.6.12-Linux/bin/iqtree"
cd $workdir
for f in *fasta
do
    $iqtree -s $f -m MFP -bb 1000 -nt AUTO
done