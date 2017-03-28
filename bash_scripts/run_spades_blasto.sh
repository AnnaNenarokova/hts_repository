#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=krtecek2.local:ppn=64

pe1_1="/home/nenarokova/genomes/jaculum/reads/1_1_trimmed.fastq.gz"
pe1_2="/home/nenarokova/genomes/jaculum/reads/1_2_trimmed.fastq.gz"

outdir="/home/nenarokova/genomes/jaculum/assembly/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.9.0-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 64 -o $outdir
