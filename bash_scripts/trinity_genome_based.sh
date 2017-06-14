#!/bin/bash
alignment="/media/4TB1/novymonas/transcriptome/mapping/wt_rna_mapped_sorted.bam"
outdir="/media/4TB1/novymonas/transcriptome/assembly/genome_based_trinity"

Trinity --genome_guided_bam $alignment --genome_guided_max_intron 1 --max_memory 60G --CPU 30 -output $outdir
