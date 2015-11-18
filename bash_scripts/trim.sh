#!/bin/bash
trimc_dir='/home/anna_nenarokova/Trimmomatic-0.35/'
fastq_dir='/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_1-light/'
trimc='trimmomatic-0.35.jar'
cd $fastq_dir
mkdir trim_out
adapters='adapters/TruSeq3-PE.fa'
file_fw='L004_light_Elis_R1.fq'
file_rv='L004_light_Elis_R2.fq'
trim='java -jar ' 
trim+=$trimc_dir$trimc
illumina_clip='ILLUMINACLIP:'
illumina_clip+=$adapters
illumina_clip+=':2:30:10'
$trim PE -phred33 $file_fw $file_rv trim_out/paired_out_fw trim_out/unpaired_out_fw trim_out/paired_out_rv trim_out/unpaired_out_rv $illumina_clip LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:30 > trimming.log