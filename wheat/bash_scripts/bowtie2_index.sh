#!/bin/bash
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_bases/
dir='sum_new_assembly_nbs_lrr'
mkdir $dir
cd $dir
bowtie2-build /mnt/lustre/nenarokova/wheat/new_assembly/nbs_lrr_genes/sum_nbs.fasta sum_new_assembly_nbs_lrr
