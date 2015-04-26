#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
cd /mnt/results/nenarokova/wheat/L/sum_fastq_re/sorted/A01/trim_out

VelvetOptimiser.pl -s 33 -e 63 -t 24 -f 'unpaired_out_fw.fastq unpaired_out_rv.fastq -shortPaired
paired_out_fw.fastq paired_out_rv.fastq' -o '-min_contig_lgth 200'