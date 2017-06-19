#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

fw="/home/nenarokova/genomes/blasto/blastocrithidia/transcriptome/Blastoc_spP57_1.fastq.gz"
rv="/home/nenarokova/genomes/blasto/blastocrithidia/transcriptome/Blastoc_spP57_2.fastq.gz"
trimdir='/home/kika/blastocrithidia/transcriptome/trimmed/'
name='p57'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/home/nenarokova/genomes/blasto/blastocrithidia/transcriptome/Blastoc_triat_1.fastq.gz"
rv="/home/nenarokova/genomes/blasto/blastocrithidia/transcriptome/Blastoc_triat_2.fastq.gz"
trimdir='/home/kika/blastocrithidia/transcriptome/trimmed/'
name='triat'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapters='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20
