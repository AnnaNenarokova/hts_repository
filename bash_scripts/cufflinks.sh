#!/bin/bash
cufflinks="/home/nenarokova/tools/cufflinks-2.2.1.Linux_x86_64/cufflinks"
aligment="/media/4TB1/novymonas/ncbi_annotation_submission/GCA_019188245.1_ASM1918824v1_sorted.bam"
out="/media/4TB1/novymonas/ncbi_annotation_submission/"
$cufflinks -p 30 -o $out $aligment
