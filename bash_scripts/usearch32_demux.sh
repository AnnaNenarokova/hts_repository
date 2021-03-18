#!/bin/bash

usearch32="/home/qiime1/bin/usearch11.0.667_i86linux32"

demux_dir="/home/qiime1/damian/reads/chunks_reads/demux/"

reads1_prefix='/home/qiime1/damian/reads/chunks_reads/reads1.fq.'
reads2_prefix='/home/qiime1/damian/reads/chunks_reads/reads2.fq.'
indexes_prefix='/home/qiime1/damian/reads/chunks_reads/indexes.fq.'
barfile="/home/qiime1/damian/barfile.fa"


mkdir $demux_dir
cd $demux_dir

for chunk in aa ab ac ad ae af ag ah ai
do
    reads1=$reads1_prefix$chunk
    reads2=$reads2_prefix$chunk
    indexes=$indexes_prefix$chunk
    demux_reads1=$reads1".demux"
    demux_reads2=$reads2".demux"
    $usearch32 -fastx_demux $reads1 -reverse $reads2 -index $indexes -barcodes $barfile -fastqout $demux_reads1 -output2 $demux_reads2
done

cat reads1.fq.*.demux > reads1_demux.fq
cat reads2.fq.*.demux > reads2_demux.fq