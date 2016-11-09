#!/bin/bash

dir_raw='/media/4TB1/novymonas/raw_reads/'

fw=$dir_raw'wt_S2_L001_R1_001.fastq.gz'
rv=$dir_raw'wt_S2_L001_R2_001.fastq.gz'

dir_merged="/media/4TB1/novymonas/merged_reads/"
merged=$dir_merged'wt_S2_L001.fastq.gz'
unmerged_fw=$dir_merged'wt_S2_L001_R1_001.fa'
unmerged_rv=$dir_merged'wt_S2_L001_R2_001.fa'
report=$dir_merged'wt_S2_L001.txt'
/home/nenarokova/tools/bbmap/bbmerge.sh t=32 in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t -tbo 2> $report
