#!/bin/bash

fastqc="/home/software/FastQC/fastqc"

outdir="/mnt/data/metagenomic_data/reads/fastqc/trimmed/"

#f1="/mnt/nfs/users/eliskaj/eliskaj/Ornithomya/ornitomya_bbduk_fwd.fastq"
#f2="/mnt/nfs/users/eliskaj/eliskaj/Ornithomya/ornitomya_bbduk_rev.fastq"

f1="/mnt/data/metagenomic_data/reads/trimmed/trimmed_data_janar/Eliska_Crataerina_R1_qtrim_bbduk.fastq"
f2=" /mnt/data/metagenomic_data/reads/trimmed/trimmed_data_janar/Eliska_Crataerina_R2_qtrim_bbduk.fastq"

$fastqc -o $outdir $f1 &
$fastqc -o $outdir $f2 &