#!/bin/sh

ref_set="/home/anna/bioinformatics/tools/BUSCO/busco_lineages/embryophyta_odb10"

#--mode sets the assessment MODE: genome, proteins, transcriptome
mode="proteins"

indir="/home/anna/bioinformatics/all_plant_sets/"
cd $indir

for infile in *.fas
do
    echo $infile
    outname="${infile%.*}"
    run_BUSCO.py -i $infile -o $outname -l $ref_set -m $mode
done
