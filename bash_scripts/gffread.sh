#!/bin/bash
gffread="/home/software/gffread-0.12.3.Linux_x86_64/gffread"
gtf="/mnt/data/martij04/Polyplax_transcriptome/STAR/stringtie/polyplax_star_stringtie.gtf"
gff="/mnt/data/martij04/Polyplax_transcriptome/STAR/stringtie/polyplax_star_stringtie.gff"

$gffread -o $gff $gtf