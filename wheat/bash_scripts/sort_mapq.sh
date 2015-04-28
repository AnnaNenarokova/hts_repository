#!/bin/bash
cd /mnt/results/nenarokova/wheat/L/sum_fastq_re/merged_alignments/full_alignments
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
q_alignment='../mapq_5_alignments/'$f
# samtools view -b -q 5 $f > $q_alignment
echo $q_alignment
sorted=${q_alignment%%.*}
echo $sorted
# samtools sort $q_alignment $sorted