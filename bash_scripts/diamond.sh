#!/bin/bash
query="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
db_path="/home/shared/BANK/diplonema_dataset/euglenozoa_anzhelika/all_euglenozoans.dmnd"
threads="30"
outfile="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_cand_diamond_euglenozoans.tsv"

outfmt_opts="qseqid qlen sseqid slen length evalue bitscore"
diamond blastp -q $query -d $db_path -o $outfile -p $threads -f 6 $outfmt_opts --max-hsps 1

# taxonmap="/media/4TB3/ncbi/prot.accession2taxid.gz"
# taxonnodes="/media/4TB3/ncbi/taxdmp/nodes.dmp"
#diamond blastp -q $query -d $db_path -o $outfile -f 102 -p 28 --taxonmap $taxonmap --taxonnodes $taxonnodes
#-f 102 - taxonomic classification
#-f 100 - Diamond internal format
