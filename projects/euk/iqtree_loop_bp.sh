#!/bin/bash
#SBATCH --job-name=iqtree_loop
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --time=14-00:00:00
#SBATCH --mem=1000M

threads=40

module load apps/iqtree/2.1.3

workdir="/user/home/vl18625/euk/ed_markers/trees_refitted/"

cd $workdir
for f in *.faa
do
    echo $f
    iqtree -s $f iqtree2 -s alignment.aln -mset LG -madd "LG+C20,LG+C20+F" -score-diff ALL -bb 1000 -nt 1
done