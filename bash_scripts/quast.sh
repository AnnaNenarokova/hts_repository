#!/bin/bash

fasta="/Users/anna/work/blasto_local/extracted_3UTRs.fasta"
min_contig=0 
outdir="/Users/anna/work/blasto_local/3UTRs_quast_statistics/"

quast.py -o $outdir -m $min_contig $fasta
