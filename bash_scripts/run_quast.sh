#!/bin/sh

f="/home/kika/MEGAsync/blasto_project/transcriptome_assembly/trinity/lygus_lineolaris_tsa.fsa"
output="/home/kika/MEGAsync/blasto_project/transcriptome_assembly/trinity/quast_results/"

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
