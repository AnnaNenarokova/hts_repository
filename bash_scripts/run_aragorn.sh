#!/bin/bash

#aragorn -v -s -d -c -l -a -w -j -ifro<min>,<max> -t -mt -m -tv -gc -seq -br -fasta -fo -o <outfile> <filename>


inf="/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/in.fasta"
out_str="/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/out_str.txt"
# out_fa="/home/kika/Dropbox/blasto_project/jaculum/genes/tRNAs/jac_tRNAs.fasta"

#secondary structure of tRNA
aragorn -t -seq -o $out_str $inf

#primary sequence of tRNA
# aragorn -t -fo -o $out_fa $inf