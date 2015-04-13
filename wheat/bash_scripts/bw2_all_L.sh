#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l mem=15Gb
#PBS -l nodes=1:ppn=1

head_folder='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/'
bt2_base='/home/nenarokova/wheat/wheat_bw2_base_v2.2/wheat'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
cd trim_out
bowtie2 --very-sensitive-local -p 1 --reorder -x $bt2_base -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../wheat_alignment.sam
