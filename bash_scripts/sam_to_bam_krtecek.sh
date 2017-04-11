#!/bin/bash

cd /home/nenarokova/tools/samtools/bin/

samfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.sam"
bam="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_sorted.bam"

./samtools view -bS -@ 20 $samfile > $bamfile
./samtools sort -o $sorted -@ 20 $bam
./samtools index $sorted

samfile="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.sam"
bam="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_sorted.bam"

./samtools sort -o $sorted -@ 20 $bam
./samtools index $sorted
