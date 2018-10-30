#!/bin/bash
slap_mapper="/home/nenarokova/tools/SLaPMapper/SLaPMapper.pl"
genome="/media/4TB1/blastocrithidia/UTR_analysis/references/blechomonas/TriTrypDB-33_BayalaiB08-376_Genome.fasta"
reads1="/media/4TB1/blastocrithidia/UTR_analysis/references/blechomonas/reads/Blechomonas_forward_reads.fastq"
reads2="/media/4TB1/blastocrithidia/UTR_analysis/references/blechomonas/reads/Blechomonas_reverse_reads.fastq"
gff="/media/4TB1/blastocrithidia/UTR_analysis/references/blechomonas/TriTrypDB-33_BayalaiB08-376.gff"
work_dir="/media/4TB1/blastocrithidia/mapping/slap_mapping/blechomonas"

#SL="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG" #p57
#SL="ATCAGTTTCTGTACTTTATTG" #Novymonas
SL="AACTAACGCTATTATTGATACAGTTTCTGTACTATATTG" #b_ayalai
min_length="6"

cd $work_dir
ln -s $reads1 reads1.fastq
ln -s $reads2 reads2.fastq
perl $slap_mapper -g $genome -l reads1.fastq -r reads2.fastq -a $gff -i $SL -s $min_length
