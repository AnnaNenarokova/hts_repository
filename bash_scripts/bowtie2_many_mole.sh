#!/bin/bash

threads=120
module load bowtie2-2.4.1

r1="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R1_001_HKJ7TDNXX.fastq.gz"
r2="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R2_001_HKJ7TDNXX.fastq.gz"

assemblies_dir="/home/users/Myxozoa_exchange/genome_workshop/assembly/"
cd $assemblies_dir

for assembly in *
do

    echo $assembly

    assembly_dir=$assemblies_dir$assembly"/"
    fasta=$assembly_dir"assembly.fasta"
    mapping_dir=$assembly_dir"mapping/"
    mkdir $mapping_dir
    name_base=$mapping_dir$assembly"_assembly"
    bt2_base=$name_base".bt2"

    bowtie2-build --threads $threads $fasta $bt2_base

    alignment=$name_base"_bt2.sam"
    report=$name_base"_bowtie2.log"

    bowtie2 --very-fast -p $threads -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

    rm $alignment
done