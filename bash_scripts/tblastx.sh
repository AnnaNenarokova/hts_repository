#!/bin/bash
query="/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa"
subject="/media/4TB1/blastocrithidia/scaffolding/reference_genomes/leish/TriTrypDB-32_LmajorFriedlin_Genome.fasta"
db_path="/media/4TB1/blastocrithidia/scaffolding/reference_genomes/lmajor_blast"
makeblastdb -in $subject -parse_seqids -dbtype nucl -out $db_path
tblastx -query $query -db $db_path -outfmt 6 -num_threads 31
