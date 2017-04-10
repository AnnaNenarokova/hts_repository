#!/bin/bash

cd /home/nenarokova/tools/samtools/bin/

samfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.sam"
bamfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_sorted"
sorted_file=$sorted".bam"
./samtools view -bS -@ 20 $samfile > $bamfile
./samtools sort $bamfile $sorted -@ 20
./samtools index $sorted_file

samfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.sam"
bamfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_sorted"
sorted_file=$sorted".bam"
./samtools view -bS -@ 20 $samfile > $bamfile
./samtools sort $bamfile $sorted -@ 20
./samtools index $sorted_file
