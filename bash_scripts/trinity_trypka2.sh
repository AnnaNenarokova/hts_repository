#!/bin/bash

r1="/media/4TB1/blasto/blastocrithidia/transcriptome/trimmed/p57_trimmed_1.fq.gz"
r2="/media/4TB1/blasto/blastocrithidia/transcriptome/trimmed/p57_trimmed_2.fq.gz"
outdir="/media/4TB1/blasto/trinity_denovo"
Trinity --seqType fq --left $r1 --right $r2 --CPU 30 --max_memory 60G --output $outdir

Trinity --genome_guided_bam p57_bw2_sorted.bam --genome_guided_max_intron 1 --max_memory 60G --CPU 30
