#!/bin/bash

threads=16

bw2_dir="/home/nenarokova/tools/bowtie2-2.2.9/"
fasta="/media/4TB1/blastocrithidia/UTR_analyisis/references/tbrucei/TriTrypDB-34_TbruceiTREU927_Genome.fasta"
bt2_base="/media/4TB1/blastocrithidia/UTR_analyisis/references/tbrucei/TriTrypDB-34_TbruceiTREU927"
$bw2_dir"bowtie2-build" --threads $threads $fasta $bt2_base

file_path="/media/4TB1/blastocrithidia/UTR_analyisis/references/tbrucei/SRR1136853"
r1="/media/4TB1/blastocrithidia/UTR_analyisis/references/tbrucei/SRR1136853_1.fastq"
r2="/media/4TB1/blastocrithidia/UTR_analyisis/references/tbrucei/SRR1136853_2.fastq"

alignment=$file_path".sam"
report=$file_path".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$file_path"_unsorted.bam"
sorted_file=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $bamfile
samtools sort -o $sorted_file -@ $threads $bamfile
samtools index -b $sorted_file
