#!/bin/bash
stringtie="/home/nenarokova/tools/stringtie-1.3.3b.Linux_x86_64/stringtie"

alignment="/media/4TB1/novymonas/transcriptome/mapping/wt_rna_mapped_sorted.bam"
out="/media/4TB1/novymonas/transcriptome/mapping/stringtie.gff"
$stringtie $alignment -p 15 -o $out

alignment="/media/4TB1/blastocrithidia/mapping/p57_star_RNA/Aligned.sortedByCoord.out.bam"
out="/media/4TB1/blastocrithidia/transcriptome_assembly/stringtie/stringtie.gff"

$stringtie $alignment -p 15 -o $out -j 20 -a 30


stringtie="/home/nenarokova/tools/stringtie-1.3.3b.Linux_x86_64/stringtie"

alignment="/media/4TB1/blastocrithidia/mapping/p57_ra_polished/illumina/p57_ra_polished_rna_sorted.bam"
out="/media/4TB1/blastocrithidia/mapping/transcript_annotation/stringtie/p57_ra_polished.gff"
$stringtie $alignment -p 32 -o $out