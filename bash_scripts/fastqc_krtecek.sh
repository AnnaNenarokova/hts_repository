#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30
reads1="/home/nenarokova/genomes/novymonas/raw_illumina/E262_1.fastq.gz"
reads2="/home/nenarokova/genomes/novymonas/raw_illumina/E262_2.fastq.gz"
reads3="/home/nenarokova/genomes/novymonas/raw_illumina/E262_1_paired_import_trimmed_F.fastq"
reads4="/home/nenarokova/genomes/novymonas/raw_illumina/E262_1_paired_import_trimmed_R.fastq"

/home/nenarokova/tools/FastQC/fastqc $reads1 -t 30 &

/home/nenarokova/tools/FastQC/fastqc $reads2 -t 30 &

/home/nenarokova/tools/FastQC/fastqc $reads1 -t 30 &

/home/nenarokova/tools/FastQC/fastqc $reads2 -t 30
