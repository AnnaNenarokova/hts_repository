#!/bin/bash
query="/media/4TB3/dpapillatum/Dp_PB-MI_190104_dedup_cut_l100.faa"

db_path="/media/4TB3/ncbi/nr_diamond.dmnd"
threads="28"
outfile="/media/4TB3/dpapillatum/dpapi_genome_diamond.out"
taxonmap="/media/4TB3/ncbi/prot.accession2taxid.gz"
taxonnodes="/media/4TB3/ncbi/taxdmp/nodes.dmp"

diamond blastp -q $query -d $db_path -o $outfile -f 100 -p 28
#diamond blastp -q $query -d $db_path -o $outfile -f 102 -p 28 --taxonmap $taxonmap --taxonnodes $taxonnodes
#-f 102 - taxonomic classification
#-f 100 - Diamond internal format
