#!/bin/bash

f="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/all_tRNAs_cleaned_90_aligned.fasta"

iqtree -s $f -m TEST -bb 1000 -T 1
