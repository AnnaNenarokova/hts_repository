#!/bin/bash

hmmdb_path="/Users/anna/work/euk_local/NCBI_COGs_Oct2020.hmm"

fasta_path="/Users/anna/work/euk_local/UP000011083_1257118.fasta"

output="/Users/anna/work/euk_local/hmm_reports/UP000011083_hout.txt"

e_threshold="0.00001"

hmmsearch -E $e_threshold -o $output $hmmdb_path $fasta_path
