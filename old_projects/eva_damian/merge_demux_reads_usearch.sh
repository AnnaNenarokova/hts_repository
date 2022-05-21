#!/bin/bash
reads1="/home/qiime1/damian/reads/reads1_demux.fq"
reads2="/home/qiime1/damian/reads/reads2_demux.fq"
dir_merged="/home/qiime1/damian/reads/usearch_merge_out/"

name='demux_reads'

merged=$dir_merged$name'_merged.fq'
report=$dir_merged$name'_merge_report.txt'
alnout=$dir_merged$name'_merged_align.txt'
tabbedout=$dir_merged$name'_merged_tab.txt'

usearch -fastq_mergepairs $reads1 -reverse $reads2 -fastq_maxdiffs 20 -fastq_maxdiffpct 50 -fastq_minmergelen 400 -fastq_maxmergelen 450 -fastq_minovlen 70 -relabel @ -fastqout $merged -report $report -alnout $alnout -tabbedout $tabbedout

info_merged=$dir_merged$name"info_merged.txt"

usearch -fastx_info $merged -output $info_merged