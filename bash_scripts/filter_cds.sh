#!/bin/bash
cd /home/anna/bioinformatics/all_tryp_references/cds
for f in *CDSs.fasta
do
    /home/anna/bioinformatics/code/ngs/py_scripts/bioscripts/filter_cds.py $f
done
