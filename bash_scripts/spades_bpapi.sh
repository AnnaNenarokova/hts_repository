#!/bin/bash

pe1="/media/4TB1/blastocrithidia/reads/genome/b_papi/B_papi_1.fastq.gz"
pe2="/media/4TB1/blastocrithidia/reads/genome/b_papi/B_papi_2.fastq.gz"

outdir="/media/4TB1/blastocrithidia/genome_assembly/b_papi/"
report=$outdir"spades_report.txt"

spades="/home/nenarokova/tools/SPAdes-3.15.2-Linux/bin/spades.py"

$spades -m 128 -1 $pe1 -2 $pe2 -t 40 -o $outdir 
