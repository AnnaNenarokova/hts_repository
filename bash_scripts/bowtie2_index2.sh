#!/bin/bash
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_bases/
dir='new_assembly_nbs_lrr_ids'
mkdir $dir
cd $dir
bowtie2-build /mnt/lustre/nenarokova/wheat/new_assembly/nbs_lrr_genes/nbs_lrr_new_assembly.fasta new_assembly_nbs_lrr_ids
