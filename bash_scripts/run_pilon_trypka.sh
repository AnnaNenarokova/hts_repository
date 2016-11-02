#!/bin/bash
cd /home/nenarokova/tools/pilon/target/scala-2.11
genome="/home/nenarokova/genomes/Trypanoplasma_borreli/miniasm/contigs.fasta"
bam="/media/4TB3/trypanoplasma/pacbio_read_mapping.bam"
outdir="/media/4TB3/trypanoplasma/pilon_out"
output="trypanoplasma"

java -Xmx16G -jar pilon_2.11-1.20-one-jar.jar --genome $genome --output $output --outdir $outdir --bam $bam --threads 32 --verbose
