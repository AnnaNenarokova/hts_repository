#!/bin/bash
adapter='/home/anna/bioinformatics/wheat/adapter.fasta'
outfile='/home/anna/bioinformatics/wheat/H7_1/H7_1.csv'
blast_db='/home/anna/bioinformatics/wheat/H7_1/db_folder/H7_1.db'
blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short -num_threads 8