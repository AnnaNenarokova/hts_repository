#!/bin/bash

reference="/home/users/nenarokova/ku_leishmania/LmxM379-SNV.fa"
mapping_dir="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/"

cd $mapping_dir
for alignment in *.bam
do
    mpileup=$alignment".mpileup"
    samtools mpileup -g -f $reference $alignment > $mpileup &
done
