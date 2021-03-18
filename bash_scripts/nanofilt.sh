#!/bin/bash

outdir="/home/users/Myxozoa_exchange/genome_workshop/filtering/"
min_qual=7
reads="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/May14_Nanopore_FG1901/FG1901_PAD09615_20190130_porechop.fastq.gz"
filtered_reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/raw_reads_min_qual_7.fq"

gunzip -c $reads | NanoFilt -q $min_qual > $filtered_reads
gunzip -c $reads | NanoFilt -q $min_qual | gzip 