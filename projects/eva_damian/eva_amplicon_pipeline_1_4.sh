#!/bin/bash
barfile="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/bar.fa"
raw_reads1="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R1_001.fastq"
reads2="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R2_001.fastq"
index_2="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_I1_001.fastq"

workdir="/home/qiime1/damian/new_results/" # don't forget the "/" at the end of the directory name
reads_dir=$workdir"reads/"

threads=23

silva_blastdb="/home/qiime1/DB/silva132_20_03_21/silva_blastdb"

mkdir $workdir
mkdir $reads_dir

source activate qiime1.9
usearch32="/home/qiime1/bin/usearch11.0.667_i86linux32"

## 3. Prepare the index files ##
echo "Preparing index files"
index1_dir=$reads_dir"I1_R1/"

echo "Extracting barcodes"
#extract_barcodes.py -f $raw_reads1 -c barcode_single_end --bc1_len 12 -o $index1_dir

reads1=$index1_dir"reads.fastq"
index_1=$index1_dir"barcodes.fastq"

indexes=$reads_dir"indexes.fq"
echo "Joining indexes"
#usearch -fastq_join $index_1 -reverse $index_2 -fastqout $indexes

##  Sorting reads  ##
echo "Sorting reads"
reads1_sorted=$reads_dir"reads1_sorted.fq"
reads2_sorted=$reads_dir"reads2_sorted.fq"
indexes_sorted=$reads_dir"indexes_sorted.fq"

#cat $reads1| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $reads1_sorted
#cat $reads2| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $reads2_sorted
#cat $indexes| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $indexes_sorted

indexes=$indexes_sorted
reads1=$reads1_sorted
reads2=$reads2_sorted

## Split the files into chunks so usearch32 can work with them ##
echo "Splitting files into chunks"

chunk_size=4000000
chunks_dir=$reads_dir"chunks_reads/"
mkdir $chunks_dir
echo $indexes
file_lines=$(cat $indexes | wc -l)
chunk_number=$(expr $file_lines / $chunk_size)

indexes_prefix=$chunks_dir"indexes.fq."
reads1_prefix=$chunks_dir"reads1.fq."
reads2_prefix=$chunks_dir"reads2.fq."

#split -x -l $chunk_size $indexes $indexes_prefix
#split -x -l $chunk_size $reads1 $reads1_prefix
#split -x -l $chunk_size $reads2 $reads2_prefix

## 4. Demultiplexing ##
echo "Demultiplexing"
cd $chunks_dir

for i in $(seq 1 $chunk_number)
do
    echo $i
    chunk=$(printf '%0*x' 2 $i)
    echo $chunk
    reads1=$reads1_prefix$chunk
    reads2=$reads2_prefix$chunk
    indexes=$indexes_prefix$chunk
    demux_reads1=$reads1".demux"
    demux_reads2=$reads2".demux"
    #$usearch32 -fastx_demux $reads1 -reverse $reads2 -index $indexes -barcodes $barfile -fastqout $demux_reads1 -output2 $demux_reads2
done
