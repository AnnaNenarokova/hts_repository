#!/bin/bash

pe1="/mnt/data/metagenomic_data/reads/trimmed/K22b_R1_bbdukVH.fastq.gz"
pe2="/mnt/data/metagenomic_data/reads/trimmed/K22b_R2_bbdukVH.fastq.gz"


outdir="/mnt/data/metagenomic_data/spades_runs/K22b/"
report=$outdir"spades_report.txt"

spades="/home/software/SPAdes-3.15.0-Linux/bin/spades.py"

mkdir $outdir
$spades -m 500 -1 $pe1 -2 $pe2 --meta -t 40 -o $outdir 

#$spades --pe1 $pe1_1 --pe2 $pe1_2 --meta -t 40 -o $outdir 2> $report
