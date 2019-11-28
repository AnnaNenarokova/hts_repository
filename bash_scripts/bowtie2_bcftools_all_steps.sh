#!/bin/bash
bowtie2="/home/users/nenarokova/tools/bowtie2-2.3.5.1-linux-x86_64/bowtie2"
bcftools="/home/users/nenarokova/tools/bcftools/bin/bcftools"
bbduk="/home/users/nenarokova/tools/bbmap/bbduk.sh"

ref="/home/users/nenarokova/ku_leishmania/LmxM379-SNV.fa"

threads=30
fw="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/reads/L_mex_wt_1.fastq"
rv="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/reads/L_mex_wt_2.fastq"

trimdir="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/reads/"
name="L_mex_wt"
trimmed_fw=$trimdir$name"_trimmed_1.fq.gz"
trimmed_rv=$trimdir$name"_trimmed_2.fq.gz"
report=$trimdir$name"_trimreport.txt"
adapters="/home/users/nenarokova/tools/bbmap/resources/adapters.fa"

# $bbduk overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$threads qtrim=rl trimq=20

bt2_base="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/LmxM379-SNV.fa.bt2"

file_path="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/L_mex_wt"
r1=$trimmed_fw
r2=$trimmed_rv

alignment=$file_path".sam"
report=$file_path"_bw2_report.txt"

$bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
unsorted_bam=$file_path"_unsorted.bam"
sorted_bam=$file_path"_sorted.bam"

samtools view -bS -@ $threads $samfile > $unsorted_bam
samtools sort -o $sorted_bam -@ $threads $unsorted_bam
samtools index -b $sorted_bam

vcf=$file_path".vcf"

$bcftools mpileup -Ou -f $ref $sorted_bam | $bcftools call -mv -Ov -o $vcf
