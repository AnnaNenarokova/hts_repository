#!/bin/bash
source /home/smrtanalysis/current/etc/setup.sh

samfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_quiver_consensus3.sam"
bamfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_quiver_consensus3_unsorted.bam"
sorted="/media/4TB3/trypanoplasma/mapping/pacbio_reads_quiver_consensus3_sorted"
sorted_file=$sorted".bam"
samtools view -bS $samfile > $bamfile -@ 32
samtools sort $bamfile $sorted -@ 32
samtools index $sorted_file

chmod 644 $sorted_file
