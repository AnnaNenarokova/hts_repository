#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_bases/
dir='ScRGA-6RL1'
mkdir $dir
cd $dir
bowtie2-build /home/nenarokova/ngs/wheat/nbs_lrr_genes/ScRGA-6RL1.fasta wheat
