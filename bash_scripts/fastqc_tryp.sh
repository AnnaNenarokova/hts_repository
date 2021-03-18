#!/bin/bash
f="/media/4TB1/blastocrithidia/reads/tRNAs/trimmed/P57-cyto_trimmed.fq.gz"

fastqc="/home/nenarokova/tools/FastQC/fastqc"

outdir="/media/4TB1/blastocrithidia/reads/tRNAs/fastqc"

$fastqc -o $outdir $f 