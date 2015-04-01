#!/bin/bash
#PBS -l walltime=100:00:00
fastq_dir='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/'
# fastq_dir='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/'
cd $fastq_dir
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
mkdir trim_out
trimc_dir='/home/nenarokova/Trimmomatic-0.33/'
trimc='trimmomatic-0.33.jar'
adapters_folder='adapters/TruSeq2-PE.fa'
# adapters_folder='adapters/all_trim.fa'
adapters=$trimc_dir$adapters_folder
file_fw=$folder'_1.fastq'
file_rv=$folder'_2.fastq'
trim='java -jar ' 
trim+=$trimc_dir$trimc
illumina_clip='ILLUMINACLIP:'
illumina_clip+=$adapters
illumina_clip+=':2:30:10'
$trim PE -phred33 $file_fw $file_rv trim_out/paired_out_fw trim_out/unpaired_out_fw trim_out/paired_out_rv trim_out/unpaired_out_rv $illumina_clip LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30