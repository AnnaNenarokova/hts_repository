#!/bin/bash
trimal="/home/nenarokova/tools/trimAl/source/trimal"

al_dir="/home/nenarokova/novymonas/alignments_1_og"

cd $al_dir

for f in OG*.fa
do
    $trimal -in $f -out $f"_trimmed.phy" -phylip -nogaps
done
