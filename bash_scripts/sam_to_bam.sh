#!/bin/bash
source /home/smrtanalysis/current/etc/setup.sh

samfile="/media/4TB1/novymonas/mapping/pacbio_reads.sam"
bamfile="/media/4TB1/novymonas/mapping/pacbio_reads_unsorted.bam"
sorted="/media/4TB1/novymonas/mapping/pacbio_reads_sorted"
sorted_file=$sorted".bam"
samtools view -bS $samfile > $bamfile -@ 20
samtools sort $bamfile $sorted -@ 20
samtools index $sorted_file

chmod 644 $sorted_file
