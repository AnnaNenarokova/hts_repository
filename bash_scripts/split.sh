#!/bin/bash

chunk_size=2

file="/home/qiime1/damian/bar.fa"

file_lines=$(cat $file | wc -l )
chunk_number=$(expr $file_lines / $chunk_size )

outdir="/home/qiime1/damian/split_test/"
prefix=$outdir"bar.fa."

split -x -l $chunk_size $file $prefix

for i in $(seq 1 $chunk_number)
do 
    chunk=$(printf '%x\n' $i)
    echo $chunk
done
