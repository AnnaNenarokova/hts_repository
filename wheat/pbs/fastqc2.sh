#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb

dir_fastqc='/mnt/lustre/nenarokova/FastQC/'
cd $dir_fastqc

fastq_dir='/home/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/'

for f in $fastq_dir*1.fastq
do 
	./fastqc $f &
done
wait

for f in $fastq_dir*2.fastq
do
        ./fastqc $f &
done
wait

cd $fastq_dir
mkdir fastqc_reports
mv *.zip fastqc_reports
rm -r *_fastqc/
tar -cvf fastqc_reports.tar fastqc_reports

