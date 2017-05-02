#!/bin/bash

pe1_1="/media/4TB1/blasto/jaculum/reads/1_1_trimmed.fastq.gz"
pe1_2="/media/4TB1/blasto/jaculum/reads/1_2_trimmed.fastq.gz"

outdir="/media/4TB1/blasto/jaculum/assembly/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.10.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 30 -o $outdir
