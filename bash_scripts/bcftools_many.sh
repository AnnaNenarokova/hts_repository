#!/bin/bash
bcftools="/home/users/nenarokova/tools/bcftools/bin/bcftools"

ref="/home/users/nenarokova/ku_leishmania/LmxM379-SNV.fa"
mapping_dir="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/"
cd $mapping_dir

for bam in *.bam
do
    vcf=$bam".vcf"
    $bcftools mpileup -Ou -f $ref $bam | $bcftools call -mv -Ov -o $vcf &
done
