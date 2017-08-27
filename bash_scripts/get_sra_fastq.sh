#!/bin/sh

cold_dir="/media/4TB1/blastocrithidia/bexlh/reads/raw/cold/"
fastq-dump --split-files --gzip -O $cold_dir SRR1186295
fastq-dump --split-files --gzip -O $cold_dir SRR1186315
fastq-dump --split-files --gzip -O $cold_dir SRR1186516

non_dir="/media/4TB1/blastocrithidia/bexlh/reads/raw/non/"
fastq-dump --split-files --gzip -O $non_dir SRR1186658
fastq-dump --split-files --gzip -O $non_dir SRR1186749
fastq-dump --split-files --gzip -O $non_dir SRR1186752

heat_dir="/media/4TB1/blastocrithidia/bexlh/reads/raw/heat/"
fastq-dump --split-files --gzip -O $heat_dir SRR1186787
fastq-dump --split-files --gzip -O $heat_dir SRR1186788
fastq-dump --split-files --gzip -O $heat_dir SRR1186789