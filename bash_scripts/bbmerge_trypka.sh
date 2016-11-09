#!/bin/bash

dir_raw='/media/4TB1/novymonas/trimmed_reads/'

fw=$dir_raw'wt_S2_L001_trimmed_1P.fq'
rv=$dir_raw'wt_S2_L001_trimmed_2P.fq'

dir_merged='/media/4TB1/novymonas/merged_reads/'
name='wt_S2_L001_trimmed'
merged=$dir_merged$name'_merged.fq'
unmerged_fw=$dir_merged$name'_unmerged_1.fq'
unmerged_rv=$dir_merged$name'_unmerged_2.fq'
report=$dir_merged$name'.txt'
/home/nenarokova/tools/bbmap/bbmerge.sh t=32 in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t -tbo 2> $report
