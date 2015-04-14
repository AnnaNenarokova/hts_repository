#!/bin/bash
#PBS -l walltime=1000:00:00
#PBS -l mem=15Gb
#PBS -l nodes=1:ppn=1

bt2_base='/home/nenarokova/wheat/bw2_base_v.2.2_all/wheat'

head_folder='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/2/'
cd $head_folder

for d in */
do
	cd $d
	cd trim_out
	bowtie2 --very-sensitive-local -p 1 --reorder -x $bt2_base -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../wheat_alignment.sam > bowtie2_logs
done