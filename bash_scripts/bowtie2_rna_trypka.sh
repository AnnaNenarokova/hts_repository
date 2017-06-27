#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
base_name='/media/4TB1/novymonas/transcriptome/mapping/bowtie2_no_pand_pseudochr/no_pand_pseudochr'
ref="/home/nenarokova/genomes/novymonas/assembly/pseudochr.fasta"
$bw2_dir'bowtie2-build' --threads 20 $ref $base_name

p1_1="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/wt_rna_trimmed_1.fq.gz"
p1_2="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/wt_rna_trimmed_2.fq.gz"

alignment=$base_name".sam"
report=$base_name".txt"
unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 20 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 20
samtools sort -o $sorted -@ 20 $bamfile
samtools index $sorted_file

