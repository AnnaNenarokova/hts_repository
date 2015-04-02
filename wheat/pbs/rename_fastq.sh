#!/bin/bash
# dir='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted'
dir='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted'

cd $dir

for folder in */
do 
	cd $folder'trim_out/'
	for f in *paired_out*
	do
		# echo $f
		mv $f $f'.fastq'
	done
	cd ../../
done