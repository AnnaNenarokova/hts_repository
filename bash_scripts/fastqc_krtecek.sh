#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30

dir1="/home/nenarokova/genomes/novymonas/raw_illumina/WT_MiSeq_trimmed/with_endosym_trimmed/"
dir2="/home/nenarokova/genomes/novymonas/raw_illumina/WT_MiSeq_trimmed/without_endosym_trimmed/"

for f in $dir1*
do
    /home/nenarokova/tools/FastQC/fastqc $f -t 30 &
done

for f in $dir2*
do
    /home/nenarokova/tools/FastQC/fastqc $f -t 30 &
done
