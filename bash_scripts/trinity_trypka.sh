#!/bin/bash
r1="/home/nenarokova/ncbi/public/sra/SRR2173361_1.fastq"
r2="/home/nenarokova/ncbi/public/sra/SRR2173361_2.fastq"
outdir="/media/4TB1/blastocrithidia/bexlh/trinity_test"
Trinity --seqType fq --left $r1 --right $r2 --CPU 2 --max_memory 60G --output $outdir
