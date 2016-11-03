#!/bin/bash
cd /home/nenarokova/tools/pilon/target/scala-2.11
genome="/media/4TB3/trypanoplasma/miniasm/contigs.fasta"
bam="/media/4TB3/trypanoplasma/mapping/pacbio_reads_sorted.bam"
outdir="/media/4TB3/trypanoplasma/pilon_out/"
output="trypanoplasma"
report="/media/4TB3/trypanoplasma/pilon_out/pilon_out.txt"
java -Xmx16G -jar pilon_2.11-1.20-one-jar.jar --genome $genome --output $output --outdir $outdir --bam $bam --threads 32 &>$report
