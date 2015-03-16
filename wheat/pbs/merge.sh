#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/R1/sum_fastq/
letters=( A B C D E F G H )
n=0
for l in "${letters[@]}"
do
	for f in $l$n*.fastq
	do 
		f2=$l${f:2}
		cat $f >> $f2
		rm $f
	done
done

