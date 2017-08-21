#!/bin/sh

directory="/media/4TB1/blastocrithidia/bexlh/reads/raw/"

fastq-dump --split-files --gzip -O $directory SRR2173361
fastq-dump --split-files --gzip -O $directory SRR2170108
fastq-dump --split-files --gzip -O $directory SRR2170117