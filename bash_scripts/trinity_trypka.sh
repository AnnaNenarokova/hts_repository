#!/bin/bash
r1="/media/4TB1/blastocrithidia/bexlh/reads/raw/SRR2170108_1.fastq.gz"
r2="/media/4TB1/blastocrithidia/bexlh/reads/raw/SRR2170108_2.fastq.gz"
outdir="/media/4TB1/blastocrithidia/bexlh/trinity_test"
Trinity --seqType fq --left $r1 --right $r2 --CPU 30 --max_memory 60G --output $outdir
