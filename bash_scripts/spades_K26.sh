#!/bin/bash

se="/mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_merged.fq"
pe1="/mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_unmerged_1.fq"
pe2="/mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_unmerged_2.fq"

outdir="/mnt/data/metagenomic_data/spades_runs/K26/"
report=$outdir"spades_report.txt"

spades="/home/software/SPAdes-3.15.0-Linux/bin/spades.py"

mkdir $outdir
$spades -m 500 -s $se -1 $pe1 -2 $pe2 --meta -t 40 -o $outdir 