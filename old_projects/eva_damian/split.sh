#!/bin/bash

chunk_size=4000000

outdir="/home/qiime1/damian/reads/chunks_reads/"

indexes='/home/qiime1/damian/reads/indexes_sorted.fq'
reads1='/home/qiime1/damian/reads/reads1_sorted.fq'
reads2='/home/qiime1/damian/reads/reads2_sorted.fq'

indexes_prefix=$outdir"indexes.fq."
reads1_prefix=$outdir"reads1.fq."
reads2_prefix=$outdir"reads2.fq."

split -l $chunk_size $indexes $indexes_prefix
split -l $chunk_size $reads1 $reads1_prefix
split -l $chunk_size $reads2 $reads2_prefix