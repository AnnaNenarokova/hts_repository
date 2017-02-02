#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
base_name='/home/kika/blastocrithidia/mapping/triat_to_p57_DNA/triat_bw2'
ref="/home/kika/blastocrithidia/genome/p57_scaffolds.fa"
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

p1_1="/home/nenarokova/genomes/blasto/blastocrithidia/genome/trimmed/triat_trimmed_1.fq"
p1_2="/home/nenarokova/genomes/blasto/blastocrithidia/genome/trimmed/triat_trimmed_2.fq"

alignment=$base_name".sam"
report=$base_name".txt"
unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 20
samtools sort $bamfile $sorted -@ 20
samtools index $sorted_file
