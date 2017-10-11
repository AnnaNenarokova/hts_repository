#!/bin/sh
cd /home/nenarokova/tools/busco

infile=""
name=""
ref_set=""
mode="proteins"
#--mode sets the assessment MODE: genдome, proteins, transcriptome
cd
python scripts/run_BUSCO.py -i $infile -o $name -l $ref_set -m [MODE]
