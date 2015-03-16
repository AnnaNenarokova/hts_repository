#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb

dir_fastqc='/mnt/lustre/nenarokova/FastQC/'
cd $dir_fastqc

fastq_dir='/home/nenarokova/wheat/R1/sum_fastq/'

for folder in $fastq_dir*/
do 
	for f in $fastq_dir$folder*/trimout/*.fastq
	do 
		./fastqc $f &
	done
done
wait
