#!/bin/sh

f="/home/kika/MEGAsync/blasto_project/genome_assembly/triat_scaffolds_transc.fasta"
output="/home/kika/MEGAsync/blasto_project/genome_assembly/quast/triat_DNA_scaffolds_transcriptome/"

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
