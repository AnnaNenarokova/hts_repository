#!/bin/bash

fw="/media/4TB1/novymonas/transcriptome/raw_reads/No_AZ3_1.fastq.gz"
rv="/media/4TB1/novymonas/transcriptome/raw_reads/No_AZ3_2.fastq.gz"
trimdir="/media/4TB1/novymonas/transcriptome/trimmed_reads/"
name="azi_rna"
trimmed_fw=$trimdir$name"_trimmed_1.fq.gz"
trimmed_rv=$trimdir$name"_trimmed_2.fq.gz"
report=$trimdir$name"_report.txt"
adapters="/home/nenarokova/tools/bbmap/resources/adapters.fa"
/home/nenarokova/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20
