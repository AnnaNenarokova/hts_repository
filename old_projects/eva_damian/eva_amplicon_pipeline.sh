#!/bin/bash
source activate qiime1.9

reads_dir="/home/qiime1/damian/reads/"
barfile="/home/qiime1/damian/barfile.fa"

index_2="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_I1_001.fastq"
raw_reads1="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R1_001.fastq"
reads2="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R2_001.fastq"

index1_dir=$reads_dir"I1_R1/"

extract_barcodes.py -f $raw_reads1 -c barcode_single_end --bc1_len 12 -o $index1_dir

reads1=$index1_dir"reads.fastq"
index_1=$index1_dir"barcodes.fastq"

indexes=$reads_dir"indexes.fq"

usearch -fastq_join $index_1 -reverse $index_2 -fastqout $indexes

reads1_sorted=$reads_dir"reads1_sorted.fq"
reads2_sorted=$reads_dir"reads2_sorted.fq"
indexes_sorted=$reads_dir"indexes_sorted.fq"

cat $reads1| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $reads1_sorted &
cat $reads2| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $reads2_sorted &
cat $indexes| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $indexes_sorted &





demux_dir=$reads_dir"demux/"

mkdir $demux_dir

demux_reads1=$demux_dir"demux_reads1.fq"
demux_reads2=$demux_dir"demux_reads2.fq"


usearch32="/home/qiime1/bin/usearch11.0.667_i86linux32"
cd $demux_dir
$usearch32 -fastx_demux $reads1 -reverse $reads2 -index $indexes -barcodes $barfile -fastqout $demux_reads1 -output2 $demux_reads2


