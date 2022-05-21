#!/bin/bash
reads1="/home/qiime1/damian/reads/reads1_demux.fq"
reads2="/home/qiime1/damian/reads/reads2_demux.fq"
workdir="/home/qiime1/damian/workdir/"

name='reads'

namepath=$workdir$name

#Merging reads
merged=$namepath'_merged.fq'
report=$namepath'_merge_report.txt'
alnout=$namepath'_merged_align.txt'
tabbedout=$namepath'_merged_tab.txt'
usearch -fastq_mergepairs $reads1 -reverse $reads2 -fastq_maxdiffs 20 -fastq_maxdiffpct 50 -fastq_minmergelen 400 -fastq_maxmergelen 450 -fastq_minovlen 70 -relabel @ -fastqout $merged -report $report -alnout $alnout -tabbedout $tabbedout

# Check the merged file
info_merged=$namepath"_info_merged.txt"
usearch -fastx_info $merged -output $info_merged

##5. Sequence filtering ##

# Remove the primers (in our datasets only R1 has primers in the sequence, 31 bp long after removing the 12 bp barcodes)
trim_merged=$namepath'_trim_merged.fq'
# Remove the primers (in our datasets only R1 has primers in the sequence, 31 bp long after removing the 12 bp barcodes)
usearch -fastx_truncate $merged -stripleft 31 -fastqout $trim_merged

info_trim_merged=$namepath"_info_trim_merged.txt"
# Check the file without primers
usearch -fastx_info $trim_merged -output $info_trim_merged

# Filter and trim the reads according to the parameters of the previous step
final_reads=$namepath"_final.fq"
usearch -fastq_filter $trim_merged -fastq_maxee 5 -fastq_trunclen 357 -fastaout $final_reads

##6. Create the OTU table (otutable97.txt)##

# Make a representative set of sequences for OTU picking in three steps
derep_reads=$namepath"_derep.fa"
derep2_reads=$namepath"_derep2.fa"
otus=$namepath"_otus_repset97.fa"
usearch -fastx_uniques $final_reads -fastaout $derep_reads -sizeout usearch -sortbysize $derep_reads -fastaout $derep2_reads -minsize 2 usearch -cluster_otus $derep2_reads -otus $otus -relabel OTU_

# Generate the OTU table from the original reads in two steps
final_reads_fasta=$namepath"_final.fa"
usearch -fastq_filter $final_reads -fastaout $final_reads_fasta
otutable=$namepath"_otutable97.txt"
usearch -usearch_global $final_reads_fasta -db $otus -id 0.97 -strand plus -otutabout $otutable
