#!/bin/bash
slap_mapper="/home/nenarokova/tools/SLaPMapper/SLaPMapper.pl"
genome="/media/4TB1/blastocrithidia/genome_assembly/p57_ra_polished.fa"
reads1="/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/p57_both_rna_trimmed_1.fq"
reads2="/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/p57_both_rna_trimmed_2.fq"
gff="media/4TB1/blastocrithidia/mapping/slap_mapping/p57_new_assembly_both_rna/p57_ra_polished.gff"
work_dir="/media/4TB1/blastocrithidia/mapping/slap_mapping/p57_new_assembly_both_rna/"

SL="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG" #p57
#SL="ATCAGTTTCTGTACTTTATTG" #Novymonas
min_length="6"

cd $work_dir
ln -s $reads1 reads1.fastq
ln -s $reads2 reads2.fastq
perl $slap_mapper -g $genome -l reads1.fastq -r reads2.fastq -a $gff -i $SL -s $min_length
