#!/bin/bash
fasta="/media/4TB3/ncbi/nr.gz"
taxonmap="/media/4TB3/ncbi/prot.accession2taxid.gz"
taxonnodes="/media/4TB3/ncbi/taxdmp.zip"
db_path="/media/4TB3/ncbi/nr_diamond.dmnd"

diamond makedb --in $fasta --db $db_path --taxonmap $taxonmap --taxonnodes $taxonnodes
