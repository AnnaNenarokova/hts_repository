#!/bin/bash
module load apps/iqtree/2.1.3

workdir="/user/home/vl18625/euk/ed_markers/trees_refitted/"

cd $workdir

file=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $file

iqtree2 -s $file-mset LG -madd "LG+C20,LG+C20+F" -score-diff ALL -bb 1000 -nt AUTO
