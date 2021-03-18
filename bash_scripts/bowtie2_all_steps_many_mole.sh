#!/bin/bash

threads=40
module load bowtie2-2.4.1

r1="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R1_001_HKJ7TDNXX.fastq.gz"
r2="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R2_001_HKJ7TDNXX.fastq.gz"

assemblies_dir="/home/users/Myxozoa_exchange/genome_workshop/assembly/"
cd $assemblies_dir


for assembly in */
do

    echo $assembly
    name=$assembly

    bowtie2-build --threads $threads $fasta $bt2_base



    alignment=$file_path".sam"
    report=$file_path".txt"

    bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

    samfile=$alignment
    bamfile=$file_path"_unsorted.bam"
    sorted_file=$file_path"_sorted.bam"

    samtools view -bS -@ $threads $samfile > $bamfile
    samtools sort -o $sorted_file -@ $threads $bamfile
    samtools index -b $sorted_file
done




