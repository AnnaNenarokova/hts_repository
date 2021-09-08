#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load diamond2

fasta="/home/users/Myxozoa_exchange/Anush/proteoms_v1/Sphaerospora_molnari_G.faa"

threads="40"

db_path="/home/users/nenarokova/myxo/smol_dmnd_db"

diamond makedb --in $fasta --db $db_path --threads $threads

outfile="/home/users/nenarokova/myxo/smol_smol_dmnd.tsv"

diamond blastp -q $fasta -d $db_path -o $outfile -f 6 -p $threads --ultra-sensitive
