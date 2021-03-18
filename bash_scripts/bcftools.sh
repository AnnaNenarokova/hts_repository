#!/bin/bash

reference="/home/users/nenarokova/ku_leishmania/LmxM379-SNV.fa"
mapping_dir="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/"

cd $mapping_dir
for alignment in *.bcf
do
    vcf=$alignment".vcf"
    bcftools view
done
