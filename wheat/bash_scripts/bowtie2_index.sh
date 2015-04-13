#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_base_v.2.2_all/
bowtie2-build /mnt/lustre/nenarokova/wheat/Taestivum_296_v2.fa wheat
