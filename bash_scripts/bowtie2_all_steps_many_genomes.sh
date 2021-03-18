#!/bin/bash

threads=40

assembly_dir="/home/users/Myxozoa_exchange/genome_workshop/assembly/"
trimdir="/media/4TB1/lmexicana_ku/reads/trimmed/"


fastas=()

for fasta in ${fastas[@]}
do


    echo $fasta
    name=$fasta


    bowtie2-build --threads $threads $fasta $bt2_base
    file_path=$mapping_dir$f

    r1=$trimdir$name"_trimmed_1.fq.gz"
    r2=$trimdir$name"_trimmed_2.fq.gz"

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




