#!/bin/bash
cufflinks="/home/nenarokova/tools/cufflinks-2.2.1.Linux_x86_64/cufflinks"
aligment="/media/4TB1/blastocrithidia/mapping/p57_RNA_to_DNA/p57_bw2_sorted.bam"
outdir="/media/4TB1/blastocrithidia/mapping/cufflinks/"
$cufflinks -p 30 -o $outdir $aligment
