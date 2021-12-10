#!/bin/bash

threads=30

fasta="/media/4TB1/novymonas/ncbi_annotation_submission/GCA_019188245.1_ASM1918824v1_genomic.fna"
bt2_base="/media/4TB1/novymonas/ncbi_annotation_submission/GCA_019188245.1_ASM1918824v1.bt2"

bowtie2-build --threads $threads $fasta $bt2_base

file_path="/media/4TB1/novymonas/ncbi_annotation_submission/GCA_019188245.1_ASM1918824v1"
r1_1="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/wt_rna_trimmed_1.fq.gz"
r1_2="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/wt_rna_trimmed_2.fq.gz"
r2_1="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/azi_rna_trimmed_1.fq.gz"
r2_2="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/azi_rna_trimmed_2.fq.gz"

alignment=$file_path".sam"
report=$file_path".txt"

bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1_1,$r2_1 -2 $r1_2,$r2_2 -S $alignment 2> $report

samfile=$alignment
unsorted_bam=$file_path"_unsorted.bam"
sorted_bam=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $unsorted_bam
samtools sort -o $sorted_bam -@ $threads $unsorted_bam
samtools index -b $sorted_bam

