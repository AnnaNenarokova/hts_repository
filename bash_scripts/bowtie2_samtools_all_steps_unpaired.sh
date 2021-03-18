#!/bin/bash

threads=30

fasta="/media/4TB1/blastocrithidia/genome_assembly/p57_ra_polished.fa"
bt2_base="/media/4TB1/blastocrithidia/mapping/p57_ra_polished/illumina/p57_ra_polished.bt2"

# bowtie2-build --threads $threads $fasta $bt2_base

file_path="/media/4TB1/blastocrithidia/mapping/p57_ra_polished/illumina/p57_ra_polished_tRNAs_new"
reads="/media/4TB1/blastocrithidia/reads/tRNAs/trimmed/P57-cyto_trimmed.fq.gz"

unaligned=$file_path"_unaligned.fq.gz"

alignment=$file_path".sam"
report=$file_path".txt"

bowtie2 --very-sensitive -p $threads -x $bt2_base -U $reads --un-gz $unaligned -S $alignment 2> $report

samfile=$alignment
unsorted_bam=$file_path"_unsorted.bam"
sorted_bam=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $unsorted_bam
samtools sort -o $sorted_bam -@ $threads $unsorted_bam
samtools index -b $sorted_bamcd

