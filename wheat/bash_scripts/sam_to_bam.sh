#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l mem=15Gb
#PBS -l nodes=1:ppn=1

head_folder='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
for f *.sam
	do
		samtools view -bS $f > $f.bam
	done