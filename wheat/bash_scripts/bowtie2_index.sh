#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_bases/
dir='NBS_LRR_wheat_genes'
mkdir $dir
cd $dir
bowtie2-build /home/nenarokova/wheat/NBS_LRR_all_plants.fasta NBS_LRR_all_plants
