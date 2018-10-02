#!/bin/bash

threads=16

fasta="/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa"
bt2_base="/media/4TB1/blastocrithidia/mapping/bw2_indexes/p57_DNA_bw2"

#bowtie2-build --threads $threads $fasta $bt2_base

file_path="/media/4TB1/blastocrithidia/mapping/p57_both_RNA_to_DNA/p57_both_RNA"
r1="/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/p57_both_rna_trimmed_1.fq"
r2="/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/p57_both_rna_trimmed_2.fq"

alignment=$file_path".sam"
report=$file_path".txt"

bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$file_path"_unsorted.bam"
sorted_file=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $bamfile
samtools sort -o $sorted_file -@ $threads $bamfile
samtools index -b $sorted_file

