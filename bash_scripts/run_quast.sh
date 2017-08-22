#!/bin/sh

f="/home/kika/blasto_project/jaculum/transcriptome/jac_trinity.fasta"
output="/home/kika/blasto_project/jaculum/transcriptome/quast/"

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4