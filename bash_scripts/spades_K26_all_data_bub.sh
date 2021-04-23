#!/bin/bash

se1="/mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_merged.fq"
pe1_1="/mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_unmerged_1.fq"
pe1_2="/mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_unmerged_2.fq"

pe2_1="/mnt/data/metagenomic_data/reads/trimmed/trimmed_data_janar/Eliska_Crataerina_R1_qtrim_bbduk.fastq"
pe2_2=" /mnt/data/metagenomic_data/reads/trimmed/trimmed_data_janar/Eliska_Crataerina_R2_qtrim_bbduk.fastq"

outdir="/mnt/data/metagenomic_data/spades_runs/K26_all_data/"
report=$outdir"spades_report.txt"

spades="/home/software/SPAdes-3.15.0-Linux/bin/spades.py"

threads=125
ram=504

mkdir $outdir
$spades -m $ram --s1 $se1 --pe1-1 $pe1_1 --pe1-2 $pe1_2 --pe2-1 $pe2_1 --pe2-2 $pe2_2 -t $threads -o $outdir 