#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40
#SBATCH -N 1
module load diamond2

query="/home/users/nenarokova/diplonema/dpapi_recoded_for_refset.faa"
outfile="/home/users/nenarokova/diplonema/hgt_new/diamond_results/dpapi_recoded_nr_tax.tsv"
threads="125"


db_path="/home/users/nenarokova/dbs/nr_tax.dmnd"
taxonmap="/home/users/nenarokova/dbs/prot.accession2taxid.gz"
taxonnodes="/home/users/nenarokova/dbs/nodes.dmp"
diamond blastp -q $query -d $db_path -o $outfile -b12 -c1 -f 102 -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes
