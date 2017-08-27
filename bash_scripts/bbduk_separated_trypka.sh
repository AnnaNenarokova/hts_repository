#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/SRR1186295_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/SRR1186295_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/cold/'
name='SRR1186295'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/SRR1186315_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/SRR1186315_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/cold/'
name='SRR1186315'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/SRR1186516_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/SRR1186516_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/cold/'
name='SRR1186516'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20