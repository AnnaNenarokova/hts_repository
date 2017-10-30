#!/bin/sh

f="/home/kika/MEGAsync/Data/Brevimastigomonas/Trinity.fasta"
output="/home/kika/MEGAsync/Data/Brevimastigomonas/"

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
