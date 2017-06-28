#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
fw=$read_dir'lygus_sraA_trimmed_fw_upd.fq',$read_dir'lygus_sraB_trimmed_fw_upd.fq',$read_dir'lygus_sraC_trimmed_fw_upd.fq'
rv=$read_dir'lygus_sraA_trimmed_rev_upd.fq',$read_dir'lygus_sraB_trimmed_rev_upd.fq',$read_dir'lygus_sraC_trimmed_rev_upd.fq'
out_dir='/media/4TB1/blastocrithidia/bexlh/trinity_assembly_sraABC'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30