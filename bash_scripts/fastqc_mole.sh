#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=4

module load FastQC
outdir="/home/users/Myxozoa_exchange/genome_workshop/fastqc_results/"

nano_unmapped="/home/users/Myxozoa_exchange/genome_workshop/mapping/unmapped_reads.fq"

nano_reads="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/May14_Nanopore_FG1901/FG1901_PAD09615_20190130_porechop.fastq.gz"

illumina_1="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R1_001_HKJ7TDNXX.fastq.gz"
illumina_2="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/Smol_DNA_Ill/FG1901_45985-A01_GGACTCCTGTAAGGAG_L002_R2_001_HKJ7TDNXX.fastq.gz"

fastqc $nano_unmapped  --outdir=$outdir
#fastqc $nano_reads --outdir=$outdir &
#fastqc $illumina_1 --outdir=$outdir &
#fastqc $illumina_2 --outdir=$outdir 