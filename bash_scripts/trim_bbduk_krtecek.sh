#!/bin/bash

fw="/home/nenarokova/genomes/novymonas/rnaseq/raw/No_WT1_1.fastq.gz"
rv="/home/nenarokova/genomes/novymonas/rnaseq/raw/No_WT1_2.fastq.gz"
trimdir='/home/nenarokova/genomes/novymonas/rnaseq/trimmed/'
name='rna_wt1'
trimmed_fw=$trimdir$name'_trimmed_1.fq'
trimmed_rv=$trimdir$name'_trimmed_2.fq'

adapters='/home/nenarokova/tools/bbmap/resources/adapters.fa'
/home/nenarokova/tools/bbmap/bbduk.sh in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe t=20 qtrim=rl trimq=20

# /home/nenarokova/tools/bbmap/bbduk.sh in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv qtrim=rl trimq=20 usejni=t 2> $report
# bbduk.sh -Xmx1g in1=read1.fq in2=read2.fq out1=clean1.fq out2=clean2.fq ref=adapters.fa ktrim=r k=23 mink=11 hdist=1 tpe
