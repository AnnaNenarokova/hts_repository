#!/bin/bash

msa="/Users/anna/work/euk_local/cogs_arcogs/arCOGs/arcogs_nina_set/fasta/arCOG00410.fa.aligned.fasta"
cleaned_msa="/Users/anna/work/euk_local/cogs_arcogs/arCOGs/arcogs_nina_set/fasta/arCOG00410.fa.aligned_trimmed_80.fasta"
trimal -in $msa -out $cleaned_msa -resoverlap 0.80 -seqoverlap 80