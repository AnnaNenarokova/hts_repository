#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
fw=$read_dir'lygus_A1_trimmed_fw.fq',$read_dir'lygus_A2_trimmed_fw.fq',$read_dir'lygus_A3_trimmed_fw.fq',$read_dir'lygus_B1_trimmed_fw.fq',$read_dir'lygus_B2_trimmed_fw.fq',$read_dir'lygus_B3_trimmed_fw.fq',$read_dir'lygus_C1_trimmed_fw.fq',$read_dir'lygus_C2_trimmed_fw.fq',$read_dir'lygus_C3_trimmed_fw.fq',$read_dir'lygus_sraA_trimmed_fw.fq',$read_dir'lygus_sraB_trimmed_fw.fq',$read_dir'lygus_sraC_trimmed_fw.fq'
rv=$read_dir'lygus_A1_trimmed_rev.fq',$read_dir'lygus_A2_trimmed_rev.fq',$read_dir'lygus_A3_trimmed_rev.fq',$read_dir'lygus_B1_trimmed_rev.fq',$read_dir'lygus_B2_trimmed_rev.fq',$read_dir'lygus_B3_trimmed_rev.fq',$read_dir'lygus_C1_trimmed_rev.fq',$read_dir'lygus_C2_trimmed_rev.fq',$read_dir'lygus_C3_trimmed_rev.fq',$read_dir'lygus_sraA_trimmed_rev.fq',$read_dir'lygus_sraB_trimmed_rev.fq',$read_dir'lygus_sraC_trimmed_rev.fq'
out_dir='/media/4TB1/blastocrithidia/bexlh/assembly/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30