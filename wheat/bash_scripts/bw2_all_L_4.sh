#!/bin/bash
#PBS -l walltime=1000:00:00
head_folder='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/1/'
cd $head_folder
bt2_base='/home/nenarokova/wheat/bw2_base_v.2.2_all/wheat'
for d in */
do
	cd $d
	cd trim_out
	bowtie2 --very-sensitive-local -p 1 --reorder -x $bt2_base -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../wheat_alignment.sam > bowtie2_logs
done