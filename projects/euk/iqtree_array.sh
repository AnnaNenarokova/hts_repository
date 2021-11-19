#!/bin/bash

workdir="/mnt/storage/scratch/vl18625/ed_cogs_with_euks/"
iqtree="/mnt/storage/home/vl18625/tools/iqtree-1.6.12-Linux/bin/iqtree"

cd $workdir

file=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $file


$iqtree -s $file -m MFP -bb 1000 -nt 1
