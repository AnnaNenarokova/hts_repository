#!/bin/bash
reads1="/home/qiime1/damian/reads/reads1_demux.fq"
reads2="/home/qiime1/damian/reads/reads2_demux.fq"
dir_merged="/home/qiime1/damian/reads/bbmerge_out/"

name='demux_reads'
merged=$dir_merged$name'_merged.fq'
report=$dir_merged$name'_bbmerge_report.txt'
ihist=$dir_merged$name'_hist.txt'

/home/qiime1/bin/bbmap/bbmerge-auto.sh in1=$reads1 in2=$reads2 out=$merged ihist=$ihist qtrim2=t usejni=t rem -strict 2> $report
