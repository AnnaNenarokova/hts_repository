#!/bin/bash

threads=30

fasta="/media/4TB1/lmexicana_ku/genome_assembly/LmxM379-SNV.fa"
bt2_base="/media/4TB1/lmexicana_ku/mapping/LmxM379-SNV/LmxM379-SNV.fa.bt2"

bowtie2-build --threads $threads $fasta $bt2_base

file_path="/media/4TB1/blastocrithidia/mapping/p57_ra_polished/illumina_rna/p57_ra_polished_rna"
r1="/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/p57_trimmed_1.fq.gz"
r2="/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/p57_trimmed_2.fq.gz"

alignment=$file_path".sam"
report=$file_path".txt"

bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
unsorted_bam=$file_path"_unsorted.bam"
sorted_bam=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $unsorted_bam
samtools sort -o $sorted_bam -@ $threads $unsorted_bam
samtools index -b $sorted_bam

