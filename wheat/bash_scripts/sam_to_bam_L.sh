#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l mem=15Gb
#PBS -l nodes=1:ppn=1

head_folder='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
for f in *.sam
	do
		echo $f
		samtools view -bS $f > $f.bam
		samtools sort $f.bam $f_sorted
		samtools index $f_sorted.bam $f_sorted.bam.bai
	done