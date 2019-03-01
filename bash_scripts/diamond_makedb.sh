#!/bin/bash
fasta="/projects/Diplonema_genome_evolution/databases/nr/nr.gz"
taxonmap="/projects/Diplonema_genome_evolution/databases/nr/prot.accession2taxid.gz"
taxonnodes="/projects/Diplonema_genome_evolution/databases/nr/taxdmp.zip"
db_path="/projects/Diplonema_genome_evolution/databases/nr/nr_diamond.dmnd"
threads="30"
diamond makedb --in $fasta --db $db_path --taxonmap $taxonmap --taxonnodes $taxonnodes --threads $threads
