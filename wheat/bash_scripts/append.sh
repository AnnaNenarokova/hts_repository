#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00

dir='/home/nenarokova/wheat/R1_2/R1/'
cd $dir
mkdir sum_fastq_re
for d in *L003*/
do 
	cd $d
	for f in *.fastq
	do
		touch ../sum_fastq_re/$f
		cat $f >> ../sum_fastq_re/$f
	done
	cd ../
done
