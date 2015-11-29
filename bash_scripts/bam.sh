#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
cd /home/nenarokova/wheat
bedtools bamtofastq -i L00000210.BC1D3RACXX.5.bam -fq L00000210.BC1D3RACXX.5_R1.fastq -fq2 L00000210.BC1D3RACXX.5_R2.fastq
