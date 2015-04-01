#!/bin/bash
trimc_dir='/home/anna/bioinformatics/bioprograms/Trimmomatic-0.33/'
fastq_dir='/home/anna/bioinformatics/htses/katya/'
trimc='trimmomatic-0.33.jar'
cd $fastq_dir
mkdir trim_out
adapters_folder='adapters/all_trim.fa'
adapters=$trimc_dir$adapters_folder
file_fw='0sec_ACAGTG_L001_R1.fastq'
file_rv='0sec_ACAGTG_L001_R2.fastq'
trim='java -jar ' 
trim+=$trimc_dir$trimc
illumina_clip='ILLUMINACLIP:'
illumina_clip+=$adapters
illumina_clip+=':2:30:10'
$trim PE -phred33 $file_fw $file_rv trim_out/paired_out_fw trim_out/unpaired_out_fw trim_out/paired_out_rv trim_out/unpaired_out_rv $illumina_clip LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30