#!/bin/bash

infile="/media/4TB1/blastocrithidia/bexlh/reads/raw/lygus_A1.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
name='lygus_A1'
trimmed=$trimdir$name'_trimmed.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in=$infile out=$trimmed usejni=t t=32 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo qtrim=rl trimq=20