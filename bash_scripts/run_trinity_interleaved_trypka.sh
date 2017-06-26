#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/'
reads=$read_dir'testing_reads.fq'
out_dir='/media/4TB1/blastocrithidia/bexlh/trinity_testing_assembly/'

Trinity --seqType fq --single reads --run_as_paired --max_memory 100G --CPU 30