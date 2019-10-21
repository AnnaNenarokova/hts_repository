#!/bin/bash
pe1_1="/media/4TB1/novymonas/genome/reads/trimmed_reads/Novy205400_trimmed_1.fq.gz"
pe1_2="/media/4TB1/novymonas/genome/reads/trimmed_reads/Novy205400_trimmed_2.fq.gz"

contigs="/media/4TB1/novymonas/old_files/novymonas_wt_scaffolds.fa"

outdir="/media/4TB1/novymonas/genome/205400_spades/"

report=$outdir"spades_report.txt"

python2 /home/nenarokova/tools/SPAdes-3.13.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2  --untrusted-contigs $contigs -t 30 -o $outdir 2> $report
