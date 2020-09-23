#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load flye

outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye/"
reads="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/May14_Nanopore_FG1901/FG1901_PAD09615_20190130_porechop.fastq.gz"
flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40