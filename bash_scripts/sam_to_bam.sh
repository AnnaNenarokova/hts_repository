#!/bin/bash

samfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads.sam"
bamfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_unsorted.bam"
sorted="/media/4TB3/trypanoplasma/mapping/pacbio_reads_sorted.bam"
samtools view -bS $samfile > $bamfile
samtools sort $bamfile $sorted
samtools index $sorted

