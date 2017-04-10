#!/bin/bash

input="/home/anna/bioinformatics/scaffolds_bw2_sorted.bam"
insert_size_metrics="/home/anna/bioinformatics/scaffolds_bw2_sorted_insert_size_metrics.txt"
insert_size_histogram="/home/anna/bioinformatics/scaffolds_bw2_sorted_insert_size_histogram.pdf"
java -jar picard.jar CollectInsertSizeMetrics \
      I=$input \
      O=$insert_size_metrics\
      H=$insert_size_histogram.pdf \
      M=0.5

