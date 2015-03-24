#!/bin/bash
dir='/home/anna/bioinformatics/htses/katya/1/'
cd $dir
mkdir sum_fastq
for d in *_001/
do 
	cd $d
	for f in *.fastq
	do
		cat $f >> ../sum_fastq/$f
	done
	cd ../
done