#!/bin/bash
cd /media/4TB1/tritryp_ref/repeat_analysis
rm="/home/serafim/tools/RepeatMasker/RepeatMasker"

threads="30"

for f in *.fasta
do
    $rm -pa $threads -noint -xsmall -gff -excln $f
done
