#!/bin/bash
module load apps/iqtree/2.1.3

workdir="/mnt/storage/scratch/vl18625/ed_cogs_with_euks/"

cd $workdir

file=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $file

iqtree2 -s $file-mset LG -madd "LG+C20,LG+C20+F" -score-diff ALL -bb 1000 -nt AUTO
