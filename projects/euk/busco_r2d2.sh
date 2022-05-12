#!/bin/bash

conda activate busco

indir="/home/guest/eukprot/eukprot3/proteins/"
cd $indir

lineage_path="/home/guest/busco/lineages/eukaryota_odb10"

N=16  # number of threads

for f in *.fasta
do
   ((i=i%N)); ((i++==0)) && wait
   out=$f".out"
   busco -i $f -l $lineage_path -o $out -m proteins -f & 
done
