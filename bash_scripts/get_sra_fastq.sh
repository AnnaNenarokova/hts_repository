#!/bin/sh

directory="/media/4TB1/blastocrithidia/bexlh/reads/raw/"

fastq-dump --split-files -O $directory SRR2170108
fastq-dump --split-files -O $directory SRR2170117