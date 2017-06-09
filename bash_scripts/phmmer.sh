#!/bin/bash

query="/home/nenarokova/genomes/euglena/tom40/all_tom40.fasta"
subject="/home/nenarokova/genomes/euglena/blast_proteome/euglena_all_proteins.fasta"

pfam_hits="/home/nenarokova/genomes/euglena/blast_proteome/all_tom40_euglena_hits_phmmer.txt"

/home/nenarokova/tools/hmmer-3.1b2-linux-intel-x86_64/binaries/phmmer --pfamtblout $pfam_hits $query $subject
