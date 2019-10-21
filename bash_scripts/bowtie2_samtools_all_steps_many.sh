#!/bin/bash

threads=30

fasta="/media/4TB1/lmexicana_ku/genome_assembly/LmxM379-SNV.fa"
bt2_base="/media/4TB1/lmexicana_ku/mapping/LmxM379-SNV/LmxM379-SNV.fa.bt2"

# bowtie2-build --threads $threads $fasta $bt2_base

mapping_dir="/media/4TB1/lmexicana_ku/mapping/LmxM379-SNV/"
trimdir="/media/4TB1/lmexicana_ku/reads/trimmed/"

files=( EEP_KO1_cl2 EEP_KO2_pop1 L_mexicana_LmxM.28.0090_KO L_mexicana_LmxM.16.0790_KO Lmex_Ku70_cl_9 Lmex_Ku80_cl_2 )

for f in ${files[@]}
do
    echo $f
    name=$f
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
