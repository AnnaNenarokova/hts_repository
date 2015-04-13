#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/wheat_bw2_base_v2.2/
bowtie2-build /mnt/lustre/nenarokova/wheat/Taestivum_296_v2.2.cds_primaryTranscriptOnly.fa wheat
