#!/bin/bash

cd /home/nenarokova/tools/samtools/bin/

bam="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_sorted.bam"

./samtools sort -o $sorted -@ 20 $bam
./samtools index $sorted

bam="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq.bam"
sorted="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_sorted.bam"

./samtools sort -o $sorted -@ 20 $bam
./samtools index $sorted
