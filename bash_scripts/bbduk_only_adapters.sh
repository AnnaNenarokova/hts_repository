#!/bin/bash

bbduk="/home/software/bbmap/bbduk.sh"
fw="/mnt/data/metagenomic_data/reads/raw/K26_GCTTGTCA-GTATGTTC_L002_R1_001.fastq.gz"
rv="/mnt/data/metagenomic_data/reads/raw/K26_GCTTGTCA-GTATGTTC_L002_R2_001.fastq.gz"
trimdir='/mnt/data/metagenomic_data/reads/trimmed/'
name='K26'
trimmed_fw=$trimdir$name'_adapter_trimmed_1.fq'
trimmed_rv=$trimdir$name'_adapter_trimmed_2.fq'

adapters='/home/software/bbmap/resources/adapters.fa'
threads=40
$bbduk in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe t=$threads #only adapter trimming
