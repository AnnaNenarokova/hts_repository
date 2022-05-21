#!/bin/bash
query_path="/home/nenarokova/amoebozoa/AmoebozoaOnlySSUHomeDatabase_all.fna"
db_path="/home/blastdb/nt_v5"
outpath="/home/nenarokova/amoebozoa/home_db_nt_v5_blastout.tsv"
threads=125
max_target_seqs=1

blastn -query $query_path -db $db_path -max_target_seqs $max_target_seqs -num_threads $threads -out $outpath -outfmt "6 qseqid qlen sseqid stitle slen length evalue pident bitscore mismatch gaps qstart qend sstart send"
