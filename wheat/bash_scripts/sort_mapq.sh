#!/bin/bash
cd /mnt/results/nenarokova/wheat/R/sum_fastq_re/merged_alignments/full_alignments
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
q50_alignment='../mapq_50_alignments/'$f
echo $q50_alignment
samtools view -q 20 $f > $q50_alignment