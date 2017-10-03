#!/bin/sh

f="/home/kika/MEGAsync/blasto_project/transcriptome_assembly/trinity/lhes2_PRJNA284294_trinity.fasta"
output="/home/kika/MEGAsync/blasto_project/transcriptome_assembly/trinity/quast_results/lhes2_PRJNA284294/"

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
