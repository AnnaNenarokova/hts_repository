#!/bin/bash
query="/home/nenarokova/blasto/p57_DNA_scaffolds.fa"
subject="/home/nenarokova/blasto/TriTrypDB-32_LmajorFriedlin_Genome.fasta"
db_path="/home/nenarokova/blasto/lmajor_blast"
makeblastdb -in $subject -parse_seqids -dbtype nucl -out $db_path
tblastx -query $query -db $db_path -outfmt 6 -num_threads 16
