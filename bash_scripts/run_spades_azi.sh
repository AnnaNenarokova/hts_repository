#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

se1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/azi_S1_adapter_trimmed_merged.fq"
pe1_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/azi_S1_unmerged_trimmed_1.fq"
pe1_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/azi_S2_unmerged_trimmed_1.fq"

outdir="/home/nenarokova/genomes/novymonas/assembly/azi_spades/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.9.0-Linux/bin/spades.py --s1 $se1 --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 60 -o $outdir 2> $report
