#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA238835/'
fw=$read_dir'SRR1186315_trimmed_1.fq.gz',$read_dir'SRR1186752_trimmed_1.fq.gz',$read_dir'SRR1186789_trimmed_1.fq.gz',$read_dir'SRR1186749_trimmed_1.fq.gz',$read_dir'SRR1186788_trimmed_1.fq.gz',$read_dir'SRR1186658_trimmed_1.fq.gz',$read_dir'SRR1186787_trimmed_1.fq.gz'
rv=$read_dir'SRR1186658_trimmed_2.fq.gz',$read_dir'SRR1186787_trimmed_2.fq.gz',$read_dir'SRR1186315_trimmed_2.fq.gz',$read_dir'SRR1186752_trimmed_2.fq.gz',$read_dir'SRR1186789_trimmed_2.fq.gz',$read_dir'SRR1186749_trimmed_2.fq.gz',$read_dir'SRR1186788_trimmed_2.fq.gz'
out_dir='/media/4TB1/blastocrithidia/bexlh/PRJNA238835_trinity/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30