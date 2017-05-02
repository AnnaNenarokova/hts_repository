#!/bin/bash

bw2_base="/media/4TB1/blasto/mapping/bowtie2_mapping/p57_bw2"
base_name="/media/4TB1/blasto/sl_poly_a_extracting/results/p57_trimmed_sl"
r1="/media/4TB1/blasto/sl_poly_a_extracting/results/p57_trimmed_1_SL.fq"
r2="/media/4TB1/blasto/sl_poly_a_extracting/results/p57_trimmed_2_SL.fq"

alignment=$base_name".sam"
report=$base_name".txt"
unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bw2_base -U $r1,$r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 20 $samfile > $bamfile
samtools sort -o $sorted_file -@ 20 $bamfile
samtools index -b $sorted_file
