#!/bin/bash
cd /media/4TB1/blastocrithidia/blast_searches/datasets/all_kinetoplastid_references_filtered

for f in *filtered.faa
do
    echo $f
    /home/nenarokova/ngs/py_scripts/blast/use_blast.py $f
done
