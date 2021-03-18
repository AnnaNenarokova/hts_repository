#!/bin/bash

module load bowtie2-2.4.1
threads=120

fasta="/home/users/Myxozoa_exchange/Anush/S.mol_genome/fg1901_40Mb_35x_nanocorr_3rd_assembly_pilon_polished.fasta"
bt2_base="/home/users/Myxozoa_exchange/genome_workshop/polishing/ron_assembly/ron_assembly"
bowtie2-build --threads $threads $fasta $bt2_base

r1="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R1_001_HKJ7TDNXX.fastq.gz"
r2="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R2_001_HKJ7TDNXX.fastq.gz"
alignment=$file_path".sam"
report=$file_path".txt"

bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
unsorted_bam=$file_path"_unsorted.bam"
sorted_bam=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $unsorted_bam
samtools sort -o $sorted_bam -@ $threads $unsorted_bam
samtools index -b $sorted_bam

