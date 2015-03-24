#!/bin/bash
adapter='/home/anna/bioinformatics/ngs/wheat/right_barcodes.fasta'
# adapter='/home/anna/bioinformatics/wheat/adapter.fasta'
outfile='/home/anna/bioinformatics/wheat/H7_1/H7_1.csv'
# blast_db='/home/anna/bioinformatics/wheat/H7_1/db_folder/H7_1.db'
blast_db='/home/anna/bioinformatics/htses/ERR015599/not_bsc_1/blast_db/not_bsc_1.db'
blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short -num_threads 8