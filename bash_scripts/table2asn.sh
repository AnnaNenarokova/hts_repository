#!/bin/bash

out_sqn=".sqn"
table2asn -M n -J -c w -euk -t template.sbt -gaps-min 10 -l paired-ends -i $fasta -f $gff -o $out_sqn -j "[organism=Novymonas esmeraldas][strain=E262AT.01]" -Z

