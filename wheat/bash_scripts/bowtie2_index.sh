#!/bin/bash
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_bases/
dir='nbs_lrr_new_assembly'
mkdir $dir
cd $dir
bowtie2-build /mnt/lustre/nenarokova/wheat/nbs_lrr_new_assembly.fasta nbs_lrr_new_assembly
