#!/bin/bash
module load apps/iqtree/2.1.3

workdir="/user/work/vl18625/euk/ed_markers/anna_set_results/msa_bmge_trimal_75/"

cd $workdir

file=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $file

iqtree2 -s $file -m MFP -B 1000 -nt 1
