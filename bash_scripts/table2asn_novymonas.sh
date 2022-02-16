#!/bin/bash
fasta="nesm_ncbi.fasta"
gff="nesm_edited_for_ncbi.gff"
template="template.sbt"
out_sqn="n_esmeraldas.sqn"
table2asn="/Users/vl18625/work/tools/mac.table2asn"
error_out="t2asn_errors.txt"
$table2asn -M n -J -c w -euk -t $template -gaps-min 10 -l paired-ends -i $fasta -f $gff -o $out_sqn -augustus-fix -j "[organism=Novymonas esmeraldas][strain=E262AT.01]" -Z 2> $error_out

