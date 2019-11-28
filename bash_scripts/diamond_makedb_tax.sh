#!/bin/bash
fasta="/home/users/DBS/nr.gz"
taxonmap="/home/users/DBS/prot.accession2taxid.gz"
taxonnodes="/home/users/DBS/nodes.dmp"
db_path="/home/users/DBS/nr_tax.dmnd"
threads="30"
diamond makedb --in $fasta --db $db_path --taxonmap $taxonmap --taxonnodes $taxonnodes --threads $threads
