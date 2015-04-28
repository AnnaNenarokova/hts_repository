#!/bin/bash
samtools mpileup -uf ref.fa aln1.bam aln2.bam | bcftools view -bvcg - > var.raw.bcf  
bcftools view var.raw.bcf | vcfutils.pl varFilter -D100 > var.flt.vcf  