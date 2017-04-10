#!/bin/bash
#PBS -l walltime=1000:00:00
#PBS -l nodes=krtecek2.local:ppn=64


outdir="/home/nenarokova/genomes/jaculum/assembly/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.9.0-Linux/bin/spades.py --continue -t 64 -o $outdir
