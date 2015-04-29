#!/bin/bash
cd /mnt/results/nenarokova/wheat/L/sum_fastq_re/merged_alignments/mapq_5_alignments/
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
ref='/mnt/lustre/nenarokova/wheat/new_assembly/nbs_lrr_genes/nbs_lrr_new_assembly.fasta'
var_bcf='../vcf/'${f%%.*}'.raw.bcf'
var_vcf='../vcf/'${f%%.*}'.flt.vcf'
echo $f
echo $var_bcf
echo $var_vcf
samtools mpileup -uf $ref $f -d 1000000 > $var_bcf
# bcftools view -bvcg $var_bcf > $var_bcf  
# bcftools view $var_bcf | vcfutils.pl varFilter -D 1000000 > $var_vcf 