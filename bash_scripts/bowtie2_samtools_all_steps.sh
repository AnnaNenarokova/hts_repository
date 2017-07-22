#!/bin/bash
bw2_dir="/home/nenarokova/tools/bowtie2-2.2.9/"
fasta="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/TriTrypDB-33_BayalaiB08-376_Genome.fasta"
bt2_base="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/mapping/blechomonas_genome"
$bw2_dir"bowtie2-build" --threads 30 $fasta $bt2_base

base_name="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/mapping/blechomonas_rna"
r1="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/reads/Blechomonas_forward_reads.fastq.gz"
r2="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/reads/Blechomonas_reverse_reads.fastq.gz"

alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 30 $samfile > $bamfile
samtools sort -o $sorted_file -@ 30 $bamfile
samtools index -b $sorted_file
