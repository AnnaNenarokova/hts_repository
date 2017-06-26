#!/bin/bash
subj_path="/home/kika/blastocrithidia/datasets/aa_ref_for_blasto.fa"
dbtype="prot"
formatdb -i $subj_path -o T -p T

query="/home/nenarokova/genomes/blasto/blastocrithidia/genome/p57_scaffolds_concatenated.fa"
report="/home/kika/blastocrithidia/datasets/blast_report.txt"

blastall -i $query -d $subj_path -p blastx -m 8 -e 0.01 -o $report -a 31
