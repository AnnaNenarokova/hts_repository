#!/bin/bash

base_name='/media/4TB1/blasto/mapping/bowtie2_mapping/p57_bw2'

r1="/home/nenarokova/blasto/results/p57_trimmed_1_poly_a.fq"
r2="/home/nenarokova/blasto/results/p57_trimmed_2_poly_a.fq"

alignment=$base_name".sam"
report=$base_name".txt"
unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $base_name -U $r1,$r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 20 $samfile > $bamfile
samtools sort -o $sorted_file -@ 20 $bamfile
samtools index -b $sorted_file
