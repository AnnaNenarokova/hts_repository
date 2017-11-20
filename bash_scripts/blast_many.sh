#!/bin/bash
cd /media/4TB1/blastocrithidia/blast_searches/datasets/all_filtered_proteins_20_11

for f in *.faa
do
    echo $f
    /home/nenarokova/ngs/py_scripts/blast/use_blast.py $f
done
