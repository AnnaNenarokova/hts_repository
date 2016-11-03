#!/bin/bash
source /home/smrtanalysis/current/etc/setup.sh

samfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads.sam"
bamfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_unsorted.bam"
sorted="/media/4TB3/trypanoplasma/mapping/pacbio_reads_sorted.bam"
samtools view -bS $samfile > $bamfile @ 32
samtools sort $bamfile $sorted @ 32
samtools index $sorted @ 32

chmod 644 $sorted
