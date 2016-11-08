#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30

cd /home/nenarokova/genomes/novymonas/raw_illumina/miseq_raw

f1="azi_S1_L001_R1_001.fastq.gz"
f2="azi_S1_L001_R2_001.fastq.gz"
f3="wt_S2_L001_R1_001.fastq.gz"
f4="wt_S2_L001_R2_001.fastq.gz"

/home/nenarokova/tools/FastQC/fastqc $f1 &
/home/nenarokova/tools/FastQC/fastqc $f2 &
/home/nenarokova/tools/FastQC/fastqc $f3 &
/home/nenarokova/tools/FastQC/fastqc $f4 &


