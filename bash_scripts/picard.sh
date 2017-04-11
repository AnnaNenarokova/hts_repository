#!/bin/bash
picard="/home/nenarokova/tools/picard.jar"

input="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_sorted"
bam=$input".bam"
insert_size_metrics=$input"insert_size_metrics.txt"
insert_size_histogram=$input"insert_size_histogram.pdf"
java -jar $picard CollectInsertSizeMetrics \
      I=$bam \
      O=$insert_size_metrics\
      H=$insert_size_histogram.pdf \
      M=0.5

input="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_sorted"
bam=$input".bam"
insert_size_metrics=$input"insert_size_metrics.txt"
insert_size_histogram=$input"insert_size_histogram.pdf"
java -jar $picard CollectInsertSizeMetrics \
      I=$bam \
      O=$insert_size_metrics\
      H=$insert_size_histogram.pdf \
      M=0.5
