#!/bin/bash

threads=120
fasta="/mnt/data/databases/nr.gz"
taxonmap="/mnt/data/databases/prot.accession2taxid.gz"
taxonnodes="/mnt/data/databases/taxdump/nodes.dmp"
db_path="/mnt/data/databases/nr_tax.dmnd"

diamond makedb --in $fasta --db $db_path --taxonmap $taxonmap --taxonnodes $taxonnodes --threads $threads
