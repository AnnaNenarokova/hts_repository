#!/bin/bash
raw_reads="/media/4TB1/blastocrithidia/reads/tRNAs/raw/tbrucei/Zdenek_Paris_J_022321-tRNA-seq-1_04232021/Raw_Data/2-T-brucei-cyto.fastq.gz"
trimdir="/media/4TB1/blastocrithidia/reads/tRNAs/trimmed/"
name="tbrucei-cyto"
trimmed_reads=$trimdir$name"_trimmed.fq.gz"
report=$trimdir$name"_report.txt"
threads="30"
adapters="/home/nenarokova/tools/bbmap/resources/adapters.fa"
bbduk="/home/nenarokova/tools/bbmap/bbduk.sh"
$bbduk overwrite=true in=$raw_reads out=$trimmed_reads ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$threads qtrim=rl trimq=20
