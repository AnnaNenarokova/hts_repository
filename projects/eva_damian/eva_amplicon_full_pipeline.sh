#!/bin/bash
barfile="/home/qiime1/damian/barfile.fa"
raw_reads1="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R1_001.fastq"
reads2="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_R2_001.fastq"
index_2="/home/qiime1/Eva/Miseq_Jan2021/210205_M07166.Project_Novakova-16S12-2021-02_01/1-Library_S1_L001_I1_001.fastq"

threads=24

silva_blastdb="/home/qiime1/DB/silva132_20_03_21/silva_blastdb"

reads_dir="/home/qiime1/damian/reads_new/"
workdir="/home/qiime1/damian/workdir_new/"
name='reads_test'
namepath=$workdir$name


mkdir $reads_dir
mkdir $workdir

source activate qiime1.9
usearch32="/home/qiime1/bin/usearch11.0.667_i86linux32"

## 3. Prepare the index files ##
echo "Preparing index files"
index1_dir=$reads_dir"I1_R1/"

extract_barcodes.py -f $raw_reads1 -c barcode_single_end --bc1_len 12 -o $index1_dir

reads1=$index1_dir"reads.fastq"
index_1=$index1_dir"barcodes.fastq"

indexes=$reads_dir"indexes.fq"

#usearch -fastq_join $index_1 -reverse $index_2 -fastqout $indexes

##  Sorting reads  ##
echo "Sorting reads"
reads1_sorted=$reads_dir"reads1_sorted.fq"
reads2_sorted=$reads_dir"reads2_sorted.fq"
indexes_sorted=$reads_dir"indexes_sorted.fq"

cat $reads1| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $reads1_sorted &
cat $reads2| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $reads2_sorted &
cat $indexes| paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" > $indexes_sorted &

indexes=$indexes_sorted
reads1=$reads1_sorted
reads2=$reads2_sorted

## Split the files into chunks so usearch32 can work with them ##
echo "Splitting files into chunks"

chunk_size=4000000
chunks_outdir=$reads_dir"chunks_reads/"
mkdir $chunks_outdir

indexes_prefix=$chunks_outdir"indexes.fq."
reads1_prefix=$chunks_outdir"reads1.fq."
reads2_prefix=$chunks_outdir"reads2.fq."

split -l $chunk_size $indexes $indexes_prefix
split -l $chunk_size $reads1 $reads1_prefix
split -l $chunk_size $reads2 $reads2_prefix

## 4. Demultiplexing ##
echo "Demultiplexing"
cd $chunks_outdir

for chunk in aa ab ac ad ae af ag ah ai
do
    reads1=$reads1_prefix$chunk
    reads2=$reads2_prefix$chunk
    indexes=$indexes_prefix$chunk
    demux_reads1=$reads1".demux"
    demux_reads2=$reads2".demux"
    #$usearch32 -fastx_demux $reads1 -reverse $reads2 -index $indexes -barcodes $barfile -fastqout $demux_reads1 -output2 $demux_reads2
done

reads1_demux=$workdir"reads1_demux.fq"
reads2_demux=$workdir"reads2_demux.fq"

cat reads1.fq.*.demux > $reads1_demux
cat reads2.fq.*.demux > $reads2_demux

## Merging pairedreads ##
echo "Merging paired reads"

merged=$namepath'_merged.fq'
report=$namepath'_merge_report.txt'
alnout=$namepath'_merged_align.txt'
tabbedout=$namepath'_merged_tab.txt'
usearch -fastq_mergepairs $reads1_demux -reverse $reads2_demux -fastq_maxdiffs 20 -fastq_maxdiffpct 50 -fastq_minmergelen 400 -fastq_maxmergelen 450 -fastq_minovlen 70 -relabel @ -fastqout $merged -report $report -alnout $alnout -tabbedout $tabbedout

# Check the merged file
echo "Checking merged reads"
info_merged=$namepath"_info_merged.txt"
usearch -fastx_info $merged -output $info_merged

##5. Sequence filtering ##

# Remove the primers (in our datasets only R1 has primers in the sequence, 31 bp long after removing the 12 bp barcodes)
echo "Removing primers"
trim_merged=$namepath'_trim_merged.fq'
# Remove the primers (in our datasets only R1 has primers in the sequence, 31 bp long after removing the 12 bp barcodes)
usearch -fastx_truncate $merged -stripleft 31 -fastqout $trim_merged

# Check the file without primers
echo "Checking trimmed reads"
info_trim_merged=$namepath"_info_trim_merged.txt"
usearch -fastx_info $trim_merged -output $info_trim_merged

# Filter and trim the reads according to the parameters of the previous step
echo "Filtering trimmed reads"
final_reads=$namepath"_final.fq"
final_reads_fasta=$namepath"_final.fa"
usearch -fastq_filter $trim_merged -fastq_maxee 5 -fastq_trunclen 357 -fastaout $final_reads_fasta

##6. Create the OTU table (otutable97.txt)##

# Make a representative set of sequences for OTU picking in three steps
echo "Making OTUs"
derep_reads=$namepath"_derep.fa"
derep2_reads=$namepath"_derep2.fa"
otus=$namepath"_otus_repset97.fa"
usearch -fastx_uniques $final_reads -fastaout $derep_reads -sizeout
usearch -sortbysize $derep_reads -fastaout $derep2_reads -minsize 2
usearch -cluster_otus $derep2_reads -otus $otus -relabel OTU_

# Generate the OTU table from the original reads in two steps
echo "Creating OTU table"
final_reads_fasta=$namepath"_final.fa"
otutable=$namepath"_otutable97.txt"
usearch -usearch_global $final_reads_fasta -db $otus -id 0.97 -strand plus -otutabout $otutable

blastout=$namepath"_otus_silva_blast.out"

blastn -query $otus -db $silva_blastdb -max_target_seqs 1 -outfmt "7 qseqid sseqid evalue bitscore length sstart send stitle sseq qseq" -num_threads $threads -out $blastout

blastout=$namepath"_otus_silva_blast.tsv"

blastn -query $otus -db $silva_blastdb -max_target_seqs 1 -num_threads $threads -out $blastout -outfmt "6 qseqid qlen sseqid stitle slen length evalue pident bitscore mismatch gaps qstart qend sstart send" 


