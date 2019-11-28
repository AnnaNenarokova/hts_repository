#!/bin/bash
# query="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
# db_path="/projects/Diplonema_genome_evolution/refdataset_diplonema/no_dpapi_refdataset.dmnd"
# threads="30"
# outfile="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_cand_diamond_no_dpapi_refdataset.tsv"

# query="/media/4TB1/novymonas/genome/novymonas_no_pand_scaffolds.fasta"
# db_path="/media/4TB3/ncbi/nr_diamond.dmnd"
# threads="30"
# outfile="/media/4TB1/novymonas/genome/assembly_diamond_nr.tsv"

# outfmt_opts="qseqid qlen sseqid slen length evalue bitscore"
# diamond blastp -q $query -d $db_path -o $outfile -p $threads -f 6 $outfmt_opts --max-hsps 1

# taxonmap="/media/4TB3/ncbi/prot.accession2taxid.gz"
# taxonnodes="/media/4TB3/ncbi/taxdmp/nodes.dmp"
# diamond blastp -q $query -d $db_path -o $outfile -f 102 -p 28 --taxonmap $taxonmap --taxonnodes $taxonnodes
# -f 102 - taxonomic classification
# -f 100 - Diamond internal format

# query="/home/users/nenarokova/novymonas/novymonas_no_pand_scaffolds.fasta"
# db_path="/home/users/DBS/nr_tax.dmnd"
# threads="30"
# outfile="/home/users/nenarokova/novymonas/assembly_diamond_nr.tsv"
# taxonmap="/home/users/DBS/prot.accession2taxid.gz"
# taxonnodes="/home/users/DBS/nodes.dmp"
# diamond blastx -q $query -d $db_path -o $outfile -f 102 -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes

query="/home/users/nenarokova/diplonema/Dp_190104_no_isoforms.faa"
db_path="/home/users/DBS/nr_tax.dmnd"
threads="30"
outfile="/home/users/nenarokova/diplonema/no_isoforms_diamond_nr.tsv"
taxonmap="/home/users/DBS/prot.accession2taxid.gz"
taxonnodes="/home/users/DBS/nodes.dmp"
diamond blastp -q $query -d $db_path -o $outfile -f 102 -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes
