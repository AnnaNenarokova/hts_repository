#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
mkdir /home/nenarokova/wheat/bw2_bases/CIN14/
cd /home/nenarokova/wheat/bw2_bases/CIN14/
bowtie2-build /home/nenarokova/ngs/wheat/nbs_lrr_genes/CIN14.fasta wheat
