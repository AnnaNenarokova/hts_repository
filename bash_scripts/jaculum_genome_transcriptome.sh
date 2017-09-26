#!/bin/bash

pe1_1="/media/4TB1/blastocrithidia/reads/genome/trimmed/jaculum_trimmed_1.fastq.gz"
pe1_2="/media/4TB1/blastocrithidia/reads/genome/trimmed/jaculum_trimmed_2.fastq.gz"

contigs="/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/jac_default/jac_trinity.fasta"

outdir="/media/4TB1/blastocrithidia/genome_assembly/jaculum_spades_transcriptome/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.10.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --untrusted-contigs $contigs --careful -t 30 -o $outdir 2> $report
