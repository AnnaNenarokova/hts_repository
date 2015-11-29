#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1
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

