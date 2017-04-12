#!/bin/bash
star="/home/nenarokova/tools/STAR-2.5.3a/bin/Linux_x86_64/STAR"
genome="/media/4TB1/blasto/p57_scaffolds.fa"
genome_dir="/media/4TB1/blasto/star_mapping"
r1="/media/4TB1/blasto/blastocrithidia/transcriptome/trimmed/p57_trimmed_1.fq.gz"
r2="/media/4TB1/blasto/blastocrithidia/transcriptome/trimmed/p57_trimmed_2.fq.gz"

$star --runThreadN 30 --genomeSAindexNbases 12 --runMode genomeGenerate --genomeFastaFiles $genome --readFilesCommand zcat --genomeDir
$star --runThreadN 30 --alignSJoverhangMin 30 --runMode alignReads --readFilesCommand zcat --genomeDir $genome_dir --outSAMtype BAM SortedByCoordinate --chimSegmentMin 30 --readFilesIn $r1 $r2
