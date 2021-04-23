#!/bin/bash

bbduk="/home/software/bbmap/bbduk.sh"
threads=40

fw="/mnt/data/metagenomic_data/reads/raw/PLF1_TTGGACTC-CTGCTTCC_L002_R1_001.fastq.gz"
rv="/mnt/data/metagenomic_data/reads/raw/PLF1_TTGGACTC-CTGCTTCC_L002_R2_001.fastq.gz"
trimdir='/mnt/data/metagenomic_data/reads/trimmed/'
name='PLF1'
trimmed_fw=$trimdir$name'_adapter_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_adapter_trimmed_2.fq.gz'

adapters='/home/software/bbmap/resources/adapters.fa'

$bbduk in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe t=$threads #only adapter trimming
