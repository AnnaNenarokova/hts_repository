#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00

dir='/home/nenarokova/wheat/R1_2/sum_fastq_re/'
cd $dir

for f in *1.fastq
do 
	cur_dir=${f::-7}
	mkdir $cur_dir
	mv $f $cur_dir
	f2=$cur_dir
	f2+='2.fastq'
	mv $f2 $cur_dir
done
