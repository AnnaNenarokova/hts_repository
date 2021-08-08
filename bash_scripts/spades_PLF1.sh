#!/bin/bash
se="/home/nenarokova/PLF1/reads/PLF1_adapter_trimmed_merged.fq.gz"
pe1="/home/nenarokova/PLF1/reads/PLF1_adapter_trimmed_unmerged_1.fq.gz"
pe2="/home/nenarokova/PLF1/reads/PLF1_adapter_trimmed_unmerged_2.fq.gz"

outdir="/home/nenarokova/PLF1/spades_out/"
report=$outdir"spades_report.txt"cd 

spades="/home/software/SPAdes-3.15.0-Linux/bin/spades.py"

mkdir $outdir
$spades -m 504 -s $se -1 $pe1 -2 $pe2 --meta -t 125 -o $outdir 