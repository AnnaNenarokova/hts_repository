#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/jac_rna_reads/trimmed/'
fw=$read_dir'jac_trimmed_1.fq.gz'
rv=$read_dir'jac_trimmed_2.fq.gz'
out_dir='/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/jac_trinity/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30