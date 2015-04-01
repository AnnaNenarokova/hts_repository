#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00

# dir='/home/nenarokova/wheat/R1_2/sum_fastq_re/'
dir='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/'

cd $dir

for f in *_1.fastq
do 
	cur_dir=${f%%_[12].fastq}
	mkdir $cur_dir
	mv $f $cur_dir
	f2=$cur_dir
	f2+='_2.fastq'
	mv $f2 $cur_dir
done
