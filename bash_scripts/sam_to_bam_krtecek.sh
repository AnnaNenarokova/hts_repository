#!/bin/bash
# PBS -l nodes=1:ppn=60
# PBS -l walltime=10000:00:00
cd /home/nenarokova/tools/samtools/bin/samtools

samfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.sam"
bamfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_sorted"
sorted_file=$sorted".bam"
./samtools view -bS -@ 60 $samfile > $bamfile
./samtools sort $bamfile $sorted -@ 60
./samtools index $sorted_file

samfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.sam"
bamfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_sorted"
sorted_file=$sorted".bam"
./samtools view -bS -@ 60 $samfile > $bamfile
./samtools sort $bamfile $sorted -@ 60
./samtools index $sorted_file
