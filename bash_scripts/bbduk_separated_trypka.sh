#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

fw="/media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017973_1.fastq"
rv="/media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017973_1.fastq"
trimdir='/media/4TB1/blastocrithidia/kika_workdir/ena_reads/'
name='SRR4017973'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=16 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017993_1.fastq"
rv="/media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017993_2.fastq"
trimdir='/media/4TB1/blastocrithidia/kika_workdir/ena_reads/'
name='SRR4017993'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=16 qtrim=rl trimq=20
