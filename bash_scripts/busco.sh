#!/bin/sh
busco_dir=""

infile=""
out=$infile"_out"
ref_set=$busco_dir"/lineages/eukaryota_odb9/"
mode="proteins"
#--mode sets the assessment MODE: genome, proteins, transcriptome
cd
python $busco_dir"scripts/run_BUSCO.py" -i $infile -o $out -l $ref_set -m [MODE]
