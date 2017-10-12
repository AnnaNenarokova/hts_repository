#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/kika_workdir/reads/'
fw=$read_dir'SRR4017973_trimmed_renamed_1.fq',$read_dir'SRR4017993_trimmed_renamed_1.fq'
rv=$read_dir'SRR4017973_trimmed_renamed_2.fq',$read_dir'SRR4017993_trimmed_renamed_2.fq'
out_dir='/media/4TB1/blastocrithidia/kika_workdir/trinity_assembly/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 16
