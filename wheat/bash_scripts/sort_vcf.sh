#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /mnt/results/nenarokova/wheat/R/sum_fastq_re/merged_alignments/vcf
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
/home/nenarokova/ngs/wheat/blast_parcer.py $f