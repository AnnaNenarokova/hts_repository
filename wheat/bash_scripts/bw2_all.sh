#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l mem=2Gb
#PBS -l nodes=1:ppn=1

head_folder='/mnt/results/nenarokova/wheat/L/sum_fastq_re/sorted/'
bt2_base='/home/nenarokova/wheat/NBS_LRR_wheat_genes/NBS_LRR_wheat_genes'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
cd trim_out
bowtie2 --very-sensitive-local -p 1 --reorder -x $bt2_base -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../NBS_LRR_wheat_genes.sam