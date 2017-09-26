#!/bin/bash
cufflinks="/home/nenarokova/tools/cufflinks-2.2.1.Linux_x86_64/cufflinks"
aligment="/media/4TB1/blastocrithidia/mapping/jac_genome_transc/jac_genome_transc_rna_sorted.bam"
outdir="/media/4TB1/blastocrithidia/mapping/transcript_annotation/cufflinks/jac"
$cufflinks -p 30 -o $outdir $aligment
