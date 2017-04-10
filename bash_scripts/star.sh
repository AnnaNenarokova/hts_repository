#!/bin/bash
star="/home/nenarokova/tools/STAR-2.5.3a/bin/Linux_x86_64/STAR"
genome="/media/4TB1/blasto/star_mapping/p57_scaffolds.fa"
genome_dir="/media/4TB1/blasto/star_mapping"
r1=""
r2=""
$star  [options]... --genomeDir $genome_dir --readFilesIn R1.fq R2.fq
