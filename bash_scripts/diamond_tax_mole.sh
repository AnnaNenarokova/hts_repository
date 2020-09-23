#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load diamond2

query="/home/users/nenarokova/myxo/augustus_6_annot_prot.faa"
db_path="/home/users/nenarokova/dbs/nr_tax.dmnd"
threads="40"
outfile="/home/users/nenarokova/myxo/smol_diamond_nr.tsv"
taxonmap="/home/users/nenarokova/dbs/prot.accession2taxid.gz"
taxonnodes="/home/users/nenarokova/dbs/nodes.dmp"
diamond blastp -q $query -d $db_path -o $outfile --ultra-sensitive -f 102 -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes
