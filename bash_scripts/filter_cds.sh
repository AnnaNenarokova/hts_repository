#!/bin/bash
cd /home/anna/bioinformatics/references/other_references/companion
# for f in *CDSs.fasta
for f in *proteins.fasta
do
    /home/anna/bioinformatics/code/ngs/py_scripts/bioscripts/filter_cds.py $f
done

