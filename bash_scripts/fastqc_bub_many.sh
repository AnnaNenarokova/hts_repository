#!/bin/bash

fastqc="/home/software/FastQC/fastqc"

workdir="/mnt/data/metagenomic_data/reads/raw/"
outdir="/mnt/data/metagenomic_data/reads/fastqc"

cd $workdir

for f in *.fastq.gz
do
    $fastqc -o $outdir -t 1 $f &
done
