#!/bin/bash

query="/home/nenarokova/dpapi/Dp_190104_no_isoforms_1.0.faa"
outfile="/home/nenarokova/dpapi/dpapi_no_isoforms_dmnd_tax.tsv"
threads="120"

db_path="/mnt/data/databases/nr_tax.dmnd"
taxonmap="/mnt/data/databases/prot.accession2taxid.gz"
taxonnodes="/mnt/data/databases/taxdump/nodes.dmp"

diamond blastx -q $query -d $db_path -o $outfile -b12 -c1 -f 102 -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes

diamond blastp -q $query -d $db_path -o $outfile -b12 -c1 -f 102 -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes
