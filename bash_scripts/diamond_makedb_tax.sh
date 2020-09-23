#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load diamond

fasta="/home/users/nenarokova/nr.gz"
taxonmap="/home/users/nenarokova/prot.accession2taxid.gz"
taxonnodes="/home/users/nenarokova/nodes.dmp"
db_path="/home/users/nenarokova/nr_tax.dmnd"
threads="40"
diamond makedb --in $fasta --db $db_path --taxonmap $taxonmap --taxonnodes $taxonnodes --threads $threads
