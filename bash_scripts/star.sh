#!/bin/bash
star="/home/nenarokova/tools/STAR-2.5.3a/bin/Linux_x86_64/STAR"
genome="/media/4TB1/novymonas/companion/pseudochr.fasta"
mapping_dir="/media/4TB1/novymonas/transcriptome/mapping/star_mapping"
r1="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/wt_rna_trimmed_1.fq.gz"
r2="/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/wt_rna_trimmed_2.fq.gz"

cd $mapping_dir

$star --runThreadN 30 --genomeSAindexNbases 12 --runMode genomeGenerate --genomeFastaFiles $genome --readFilesCommand zcat --genomeDir $mapping_dir
$star --runThreadN 30 --alignSJoverhangMin 30 --runMode alignReads --readFilesCommand zcat --genomeDir $mapping_dir --limitBAMsortRAM 2000000000 --outSAMtype BAM SortedByCoordinate --chimSegmentMin 30 --readFilesIn $r1 $r2
