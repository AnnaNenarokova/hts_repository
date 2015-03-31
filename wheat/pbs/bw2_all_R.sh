#!/bin/bash
#PBS -l select=1:ncpus=1
#PBS -l walltime=1000:00:00
head_folder='/home/nenarokova/wheat/R1_2/R1/sum_fastq/'
bt2_base='/mnt/lustre/nenarokova/wheat/wheat_bowtie2_index/wheat'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAY_INDEX | head -1`
cd $folder
cd trim_out
bowtie2 --local --very-fast-local -p 1 --reorder -a -x $bt2_base, -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../wheat_alignment.sam
