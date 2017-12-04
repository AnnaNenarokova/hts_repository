#!/bin/bash
cd /home/anna/bioinformatics/references/tritrypdb_references/tritrypdb_34/proteins_filtering
# for f in *CDSs.fasta
for f in *roteins.fasta
do
    /home/anna/bioinformatics/code/ngs/py_scripts/bioscripts/filter_cds.py $f
done

