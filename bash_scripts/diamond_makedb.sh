#!/bin/bash
fasta="/projects/Diplonema_genome_evolution/refdataset_diplonema/dpapi_refdataset.faa"
db_path="/projects/Diplonema_genome_evolution/refdataset_diplonema/dpapi_refdataset.dmnd"
threads="30"
diamond makedb --in $fasta --db $db_path --threads $threads
