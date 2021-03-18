#!/bin/bash

dir_raw='/media/4TB1/novymonas/trimmed_reads/'

reads_fw="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R1_001.fastq"
reads_rev="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R2_001.fastq"

dir_merged='/home/qiime1/damian/reads/bbduk/merged_reads/'
name='azi_S1_adapter_trimmed'
merged=$dir_merged$name'_merged.fq'
unmerged_fw=$dir_merged$name'_unmerged_1.fq'
unmerged_rv=$dir_merged$name'_unmerged_2.fq'
report=$dir_merged$name'.txt'
ihist=$dir_merged$name'_hist.txt'

/home/nenarokova/tools/bbmap/bbmerge-auto.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t rem extend2=50 k=62 2> $report
