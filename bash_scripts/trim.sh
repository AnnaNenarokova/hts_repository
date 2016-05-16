#!/bin/bash

cd /media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/raw_reads

trimc_dir='/home/nenarokova/tools/Trimmomatic-0.36/'

trim='java -jar '$trimc_dir'trimmomatic-0.36.jar'

p_out_fw='/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/trimmed_reads/19109_8#2_paired_out_fw.fastq'
u_out_fw='/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/trimmed_reads/19109_8#2_unpaired_out_fw.fastq'
p_out_rv='/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/trimmed_reads/19109_8#2_paired_out_rv.fastq'
u_out_rv='/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/trimmed_reads/19109_8#2_unpaired_out_rv.fastq'

log = '/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/trimmed_reads/19109_8#2_trimming.log'

file_fw='/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/raw_reads/19109_8#2_1.fastq'
file_rv='/media/4TB1/kinetoplastids_hinxton/species/cer3/illumina/raw_reads/19109_8#2_2.fastq'

$trim PE -phred33 $file_fw $file_rv $p_out_fw $u_out_fw $p_out_rv $u_out_rv LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:50
