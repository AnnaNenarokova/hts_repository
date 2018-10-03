#!/bin/bash
slap_mapper="/home/nenarokova/tools/SLaPMapper/SLaPMapper.pl"
genome="/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa"
reads1="/media/4TB1/blastocrithidia/reads/transcriptome/raw/p57_both_RNA_1.fastq"
reads2="/media/4TB1/blastocrithidia/reads/transcriptome/raw/p57_both_RNA_2.fastq"
gff="/media/4TB1/blastocrithidia/mapping/slap_mapping/p57_empty_annotation.gff"
work_dir="/media/4TB1/blastocrithidia/mapping/slap_mapping/p57_both_rna_4"

SL="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG"
min_length="4"

cd $work_dir
ln -s $reads1 reads1.fastq
ln -s $reads2 reads2.fastq
perl $slap_mapper -g $genome -l reads1.fastq -r reads2.fastq -a $gff -i $SL -s $min_length
