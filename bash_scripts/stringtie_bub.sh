#!/bin/bash
stringtie="/home/software/stringtie-2.1.4.Linux_x86_64/stringtie"


alignment="/mnt/data/martij04/Polyplax_transcriptome/STAR/Results_trimmed_reads_mapped_genome89contigs/Aligned.sortedByCoord.out.bam"
out="/mnt/data/martij04/Polyplax_transcriptome/STAR/stringtie/polyplax_star_stringtie.gtf"

threads=96

$stringtie $alignment -p $threads -o $out


