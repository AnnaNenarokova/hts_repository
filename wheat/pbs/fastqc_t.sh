#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb

dir_fastqc='/mnt/lustre/nenarokova/FastQC/'
cd $dir_fastqc

# fastq_dir='/home/nenarokova/wheat/R1/sum_fastq/'
fastq_dir='/home/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/'

for folder in $fastq_dir*/
do 
	for f in $folder*.fastq
		do
			./fastqc $f &
		done
		wait

done
wait