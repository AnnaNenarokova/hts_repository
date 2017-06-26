#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/'
fw=$read_dir'testing_reads_fw.fq'
rv=$read_dir'testing_reads_rv.fq'
out_dir='/media/4TB1/blastocrithidia/bexlh/trinity_test_assembly/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30