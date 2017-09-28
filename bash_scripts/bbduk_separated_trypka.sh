#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186295_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186295_1.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186295'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186315_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186315_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186315'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186516_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186516_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186516'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186658_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186658_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186658'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186749_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186749_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186749'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186752_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186752_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186752'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186787_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186787_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186787'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186788_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186788_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186788'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186789_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/SRR1186789_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
name='SRR1186789'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA284294/SRR2170108_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA284294/SRR2170108_1.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA284294/'
name='SRR2170108'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA284294/SRR2170117_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA284294/SRR2170117_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA284294/'
name='SRR2170117'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20

fw="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA284294/SRR2173361_1.fastq.gz"
rv="/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA284294/SRR2173361_2.fastq.gz"
trimdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA284294/'
name='SRR2173361'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'
/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=32 qtrim=rl trimq=20
