#!/bin/bash
cd /home/anna/bioinformatics/references/tritrypdb_references/tritrypdb_34/filtered_proteins_cds
for f in *_AnnotatedCDSs_filtered.fasta
do
    out=$f"_translated.faa"
    transeq -trim -sequence $f -outseq $out
done
