#!/bin/bash
cd /mnt/results/nenarokova/wheat/L/sum_fastq_re/sorted/merged_alignments/full_alignments
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
q50_alignment='../mapq_50_alignments/'$f
samtools view -q 50 $f > $q50_alignment
ref='/mnt/lustre/nenarokova/wheat/new_assembly/nbs_lrr_genes/nbs_lrr_new_assembly.fasta'
var_bcf=${q50_alignment:0:-4}'.raw.bcf'
var_vcf=${q50_alignment:0:-4}'.flt.bcf'
samtools mpileup -uf $ref $q50_alignment | bcftools view -bvcg - > $var_bcf  
bcftools view $var_bcf | vcfutils.pl varFilter -D1000000 > $var_vcf 