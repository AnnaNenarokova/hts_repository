#!/bin/bash
# trimc_dir='/home/nenarokova/Trimmomatic-0.33'
trimc_dir='/home/anna/bioinformatics/bioprograms/Trimmomatic-0.33/'
cd /home/anna/bioinformatics/htses/katya/
mkdir trim_out
# adapters_file=$trimc_dir/adapters/all_trim.fa
file_fw='0sec_ACAGTG_L001_R1.fastq'
file_rv='0sec_ACAGTG_L001_R2.fastq'
java -jar /home/anna/bioinformatics/bioprograms/Trimmomatic-0.33/trimmomatic-0.33.jar PE -phred33 $file_fw $file_rv trim_out/paired_out_fw trim_out/unpaired_out_fw trim_out/paired_out_rv trim_out/unpaired_out_rv ILLUMINACLIP:/home/anna/bioinformatics/bioprograms/Trimmomatic-0.33/adapters/TruSeq2-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30