#!/bin/bash

threads=30

bw2_dir="/home/nenarokova/tools/bowtie2-2.2.9/"
fasta=""
bt2_base="/media/4TB1/blastocrithidia/mapping/jac_genome/jac_bw2"
# $bw2_dir"bowtie2-build" --threads $threads $fasta $bt2_base

file_path="/media/4TB1/blastocrithidia/mapping/jac_genome_transc/jac_genome_DNA"
r1="/media/4TB1/blastocrithidia/reads/genome/trimmed/jaculum_trimmed_1.fastq.gz"
r2="/media/4TB1/blastocrithidia/reads/genome/trimmed/jaculum_trimmed_2.fastq.gz"

alignment=$file_path".sam"
report=$file_path".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$file_path"_unsorted.bam"
sorted_file=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $bamfile
samtools sort -o $sorted_file -@ $threads $bamfile
samtools index -b $sorted_file
