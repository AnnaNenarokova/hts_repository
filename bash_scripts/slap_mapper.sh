#!/bin/bash
slap_mapper="/home/nenarokova/tools/SLaPMapper/SLaPMapper.pl"
genome="/media/4TB1/novymonas/genome/annotation/companion_no_pand_lbraz/scafs.fasta"
reads1="/media/4TB1/novymonas/transcriptome/reads/raw_reads/No_WT1_1.fastq.gz"
reads2="/media/4TB1/novymonas/transcriptome/reads/raw_reads/No_WT1_2.fastq.gz"
gff="/media/4TB1/novymonas/genome/annotation/companion_no_pand_lbraz/scaffold.out.gff3"
work_dir="/media/4TB1/novymonas/slap_mapping/"

#SL="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG" #p57
SL="ATCAGTTTCTGTACTTTATTG" #Novymonas

min_length="6"

cd $work_dir
ln -s $reads1 reads1.fastq
ln -s $reads2 reads2.fastq
perl $slap_mapper -g $genome -l reads1.fastq -r reads2.fastq -a $gff -i $SL -s $min_length
