#!/bin/bash
# ssh smrtanalysis@172.18.4.4

source /home/smrtanalysis/current/etc/setup.sh

input="/media/4TB1/novymonas/mapping/input.fofn"
genome="/media/4TB1/novymonas/e262_hiseq_contigs.fa"

out="/media/4TB1/novymonas/mapping/pacbio_reads.sam"
unaligned="media/4TB1/novymonas/mapping/unaligned_pacbio_reads"
blasr $input $genome -sam -out $out -nproc 32 #-clipping soft #-unaligned $unaligned
