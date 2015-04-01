#!/bin/bash
#PBS -l walltime=100:00:00
trimc_dir='/home/nenarokova/Trimmomatic-0.33'
cd /home/anna/bioinformatics/htses/katya/
mkdir trim_out

fastq_dir='/home/nenarokova/wheat/R1_2/R1/sum_fastq_re/R1/'
cd $fastq_dir
file_fw=`ls -1 | tail -n $PBS_ARRAYID | head -1`
mkdir trim_out
trimc_dir='/home/nenarokova/Trimmomatic-0.33'
trimc='trimmomatic-0.33.jar'


adapters_folder='adapters/TruSeq2-PE.fa'
# adapters_folder='adapters/all_trim.fa'
adapters=$trimc_dir$adapters_folder
file_fw='0sec_ACAGTG_L001_R1.fastq'
file_rv='0sec_ACAGTG_L001_R2.fastq'
trim='java -jar ' 
trim+=$trimc_dir$trimc
illumina_clip='ILLUMINACLIP:'
illumina_clip+=$adapters
illumina_clip+=':2:30:10'
$trim PE -phred33 $file_fw $file_rv trim_out/paired_out_fw trim_out/unpaired_out_fw trim_out/paired_out_rv trim_out/unpaired_out_rv $illumina_clip LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30