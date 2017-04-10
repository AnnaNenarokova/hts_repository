#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30

# bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
# fasta='/home/nenarokova/genomes/novymonas/assembly/PROKKA_11282016.fna'
# bt2_base="/home/nenarokova/genomes/novymonas/assembly/pandoraea_genome"
# $bw2_dir'bowtie2-build' --threads 30 $fasta $bt2_base

# p1_1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq/E262_1.fastq"
# p1_2="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq/E262_2.fastq"

# mapped_reads="/home/nenarokova/genomes/novymonas/assembly/hiseq_mapped.fq"

# base_name="/home/nenarokova/genomes/novymonas/assembly/hiseq"
# alignment=$base_name".sam"
# report=$base_name".txt"

# /home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $p1_1 -2 $p1_2 --al-conc-gz $mapped_reads -S $alignment 2> $report

p1_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_raw/wt_S2_L001_R1_001.fastq.gz"
p1_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_raw/wt_S2_L001_R2_001.fastq.gz"

mapped_reads="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_mapped.fq"

base_name="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/pandoraea_genome"
alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $p1_1 -2 $p1_2 --al-conc-gz $mapped_reads -S $alignment 2> $report

