#!/bin/bash
module load apps/iqtree/2.1.3

workdir="/user/home/vl18625/euk/ed_markers/al_trimmed_man_cleaned/"

cd $workdir

file=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $file

iqtree2 -s $file -mset LG -madd "LG+C20,LG+C20+F" --score-diff all -bb 1000 -nt 1
