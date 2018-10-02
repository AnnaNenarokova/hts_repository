#!/bin/bash
trimal="/home/anna/bioinformatics/tools/trimal.v1.2rev59/trimAl/source/trimal"

in="OG0002170.marker001.OG0002170_replaced.fa.sorted.aln"

out=$in"_trimmed.aln"

$trimal -in $in -out $out -fasta -st 0.003

