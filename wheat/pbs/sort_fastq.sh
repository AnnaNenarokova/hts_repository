#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb

cd /home/nenarokova/wheat/R1
numbers=( 1 2 )
name1='0sec_ACAGTG_L001_R'
name2='_001.fastq'
for n in "${numbers[@]}"
	do 
		f=$name1$n$name2
		fastqc $f &
		echo 'fiffi'
done
wait
