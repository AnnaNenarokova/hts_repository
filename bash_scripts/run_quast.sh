#!/bin/sh

f="/home/kika/MEGAsync/Data/Chlamydomonas_amazonie/2015_DNA-seq/cam_spades_2.fasta"
output="/home/kika/MEGAsync/Data/Chlamydomonas_amazonie/2015_DNA-seq/quast_results_2/"

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4