#!/bin/bash

dir_raw='/media/4TB1/novymonas/raw_reads/'

fw=$dir_raw'azi_S1_L001_R1_001.fastq.gz'
rv=$dir_raw'azi_S1_L001_R2_001.fastq.gz'

dir_merged='/media/4TB1/novymonas/merged_reads/'
name='azi_S1'
merged=$dir_merged$name'_merged.fq'
unmerged_fw=$dir_merged$name'_unmerged_1.fq'
unmerged_rv=$dir_merged$name'_unmerged_2.fq'
report=$dir_merged$name'.txt'
/home/nenarokova/tools/bbmap/bbmerge.sh t=32 in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t -tbo 2> $report
