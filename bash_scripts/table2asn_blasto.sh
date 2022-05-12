#!/bin/bash
indir="/Users/vl18625/work/blasto_local/annotation_ncbi/LWC14/"
template="/Users/vl18625/work/blasto_local/annotation_ncbi/template.sbt"
table2asn="/Users/vl18625/work/tools/mac.table2asn"
output="/Users/vl18625/work/blasto_local/annotation_ncbi/LWC14.sqn"
$table2asn -indir $indir -t $template -gaps-min 10 -l paired-ends -o $output -Z