#!/bin/bash
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/bw2_bases/
dir='old_assembly_transcripts'
mkdir $dir
cd $dir
bowtie2-build /mnt/lustre/nenarokova/wheat/Taestivum_296_v2.2.transcript.fa transcripts2
