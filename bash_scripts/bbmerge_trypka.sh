#!/bin/bash

dir_raw='/media/4TB1/novymonas/raw_reads/'

fw=$dir_raw'azi_S1_L001_R1_001.fastq.gz'
rv=$dir_raw'azi_S1_L001_R2_001.fastq.gz'

dir_merged="/media/4TB1/novymonas/merged_reads/"
merged=$dir_merged'azi_S1_L001_merged.fa'
unmerged_fw=$dir_merged'azi_S1_L001_unmerged_1.fa'
unmerged_rv=$dir_merged'azi_S1_L001_unmerged_2.fa'
report=$dir_merged'azi_S1_L001_report.txt'
/home/nenarokova/tools/bbmap/bbmerge.sh t=32 in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t 2> $report
