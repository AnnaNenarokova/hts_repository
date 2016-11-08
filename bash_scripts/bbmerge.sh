#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=64

dir_raw='/home/nenarokova/genomes/novymonas/raw_illumina/miseq_raw/'

fw=$dir_raw'azi_S1_L001_R1_001.fastq.gz'
rv=$dir_raw'azi_S1_L001_R2_001.fastq.gz'

dir_merged="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/"
merged=$dir_merged'azi_S1_L001_merged.fa'
unmerged_fw=$dir_merged'azi_S1_L001_unmerged_1.fa'
unmerged_rv=$dir_merged'azi_S1_L001_unmerged_2.fa'
report=$dir_merged'azi_S1_L001_report.txt'
/home/nenarokova/tools/bbmap/bbmerge.sh t=64 in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t 2> $report
