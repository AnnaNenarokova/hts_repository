#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
fw=$read_dir'SRR2170108_trimmed_1.fq.gz',$read_dir'SRR2170117_trimmed_1.fq.gz',$read_dir'SRR2173361_trimmed_1.fq.gz'
rv=$read_dir'SRR2170108_trimmed_2.fq.gz',$read_dir'SRR2170117_trimmed_2.fq.gz',$read_dir'SRR2173361_trimmed_2.fq.gz'
out_dir='/media/4TB1/blastocrithidia/bexlh/transcriptome_trinity/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30