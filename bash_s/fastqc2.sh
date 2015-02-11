#!/bin/bash
cd /home/anna/bioinformatics/htses/katya

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