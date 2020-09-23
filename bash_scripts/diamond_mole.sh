#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load diamond2

query="/home/users/nenarokova/myxo/smol_augustus_6_annot_prot.faa"
db_path="/home/users/nenarokova/dbs/nr_tax.dmnd"
threads="40"
outfile="/home/users/nenarokova/myxo/smol_diamond_nr_normal.tsv"

diamond blastp -q $query -d $db_path -o $outfile -f 6 -p $threads --ultra-sensitive
