#!/bin/bash

module load diamond2
threads="120"

query="/home/users/nenarokova/diplonema/dpapi_recoded_for_refset.faa"

ref_fasta="/home/users/nenarokova/diplonema/ref_dataset/dpapi_full_dataset.faa"
ref_db_path="/home/users/nenarokova/diplonema/ref_dataset/dpapi_full_dataset.dmnd"
outfile="/home/users/nenarokova/diplonema/hgt_new/diamond_results/dpapi_refdataset_dmnd.tsv"

diamond makedb --in $ref_fasta --db $ref_db_path --threads $threads
diamond blastp -q $query -d $ref_db_path -o $outfile -f 6 -p $threads -b12 -c1

nr_db_path="/home/users/nenarokova/dbs/nr_tax.dmnd"
outfile="/home/users/nenarokova/diplonema/hgt_new/diamond_results/dpapi_nr_dmnd.tsv"

diamond blastp -q $query -d $nr_db_path -o $outfile -f 6 -p $threads -b12 -c1