#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /mnt/results/nenarokova/wheat/L/sum_fastq_re/merged_alignments/vcf/
f=`ls -1 *.flt.vcf | tail -n $PBS_ARRAYID | head -1`
/home/nenarokova/ngs/wheat/sort_vcf.py $f