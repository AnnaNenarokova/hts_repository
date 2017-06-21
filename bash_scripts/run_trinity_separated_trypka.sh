#!/bin/bash

wdir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
fw=$wdir'lygus_A1_trimmed_fw.fq',$wdir'lygus_A2_trimmed_fw.fq',$wdir'lygus_A3_trimmed_fw.fq',$wdir'lygus_B1_trimmed_fw.fq',$wdir'lygus_B2_trimmed_fw.fq',$wdir'lygus_B3_trimmed_fw.fq',$wdir'lygus_C1_trimmed_fw.fq',$wdir'lygus_C2_trimmed_fw.fq',$wdir'lygus_C3_trimmed_fw.fq',$wdir'lygus_sraA_trimmed_fw.fq',$wdir'lygus_sraB_trimmed_fw.fq',$wdir'lygus_sraC_trimmed_fw.fq'
rv=$wdir'lygus_A1_trimmed_rev.fq',$wdir'lygus_A2_trimmed_rev.fq',$wdir'lygus_A3_trimmed_rev.fq',$wdir'lygus_B1_trimmed_rev.fq',$wdir'lygus_B2_trimmed_rev.fq',$wdir'lygus_B3_trimmed_rev.fq',$wdir'lygus_C1_trimmed_rev.fq',$wdir'lygus_C2_trimmed_rev.fq',$wdir'lygus_C3_trimmed_rev.fq',$wdir'lygus_sraA_trimmed_rev.fq',$wdir'lygus_sraB_trimmed_rev.fq',$wdir'lygus_sraC_trimmed_rev.fq'

Trinity --seqType fq --left $fw --right $rv --max_memory 100G --CPU 30