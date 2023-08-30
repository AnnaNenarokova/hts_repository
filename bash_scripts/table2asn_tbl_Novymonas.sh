#!/bin/bash
table2asn="/Users/vl18625/work/tools/mac.table2asn"

fasta="/Users/vl18625/work/novymonas_ncbi/2023_08_30__attempt_1/Novymonas.fna"
tbl_file="/Users/vl18625/work/novymonas_ncbi/2023_08_30__attempt_1/Novymonas.tbl"
template_file="/Users/vl18625/work/novymonas_ncbi/2023_08_30__attempt_1/Novymonas.sbt"
out_sqn="/Users/vl18625/work/novymonas_ncbi/2023_08_30__attempt_1/Novymonas.sqn"

log="/Users/vl18625/work/novymonas_ncbi/2023_08_30__attempt_1/table2asn_2023_08_30_log.txt"


$table2asn -M n -J -c w -euk -t $template_file -gaps-min 10 -l paired-ends -j "[organism=Novymonas esmeraldas][strain=E262AT.01][gcode=1]" -i $fasta -f $tbl_file -o $out_sqn -Z 2> $log