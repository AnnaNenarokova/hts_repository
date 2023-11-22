#!/bin/bash
table2asn="/Users/vl18625/work/tools/mac.table2asn"

workdir="/Users/vl18625/work/novymonas_ncbi/20_11_2023_attempt_7_anna/"
fasta=$workdir"Novymonas.fsa"
tbl_file=$workdir"Novymonas.tbl"
template_file=$workdir"Novymonas.sbt"
out_sqn=$workdir"Novymonas.sqn"

log=$workdir"table2asn_error_log.txt"


$table2asn -t $template_file -f $tbl_file -i $fasta -o $out_sqn -c f -euk -a a -V v -Z -gaps-min 10 -l paired-ends 2> $log