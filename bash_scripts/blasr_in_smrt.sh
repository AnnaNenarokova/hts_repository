#!/bin/bash
# ssh smrtanalysis@172.18.4.4

source /home/smrtanalysis/current/etc/setup.sh

input="/media/4TB3/trypanoplasma/mapping/input.fofn"
genome="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver3.fastq"

out="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver3.sam"
unaligned="/media/4TB1/novymonas/mapping/pacbio_consensus_quiver3_unaligned.fq"

blasr $input $genome -sam -out $out -nproc 32 -clipping soft -unaligned $unaligned

samfile="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver3.sam"
bamfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_consensus3_unsorted.bam"
sorted="/media/4TB3/trypanoplasma/mapping/pacbio_reads_consensus3_sorted"
sorted_file=$sorted".bam"
mapped_file=$sorted"_mapped.bam"
samtools view -bS -@ 32 $samfile > $bamfile
samtools sort $bamfile $sorted -@ 32
samtools index $sorted_file
