#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load diamond2

fasta="/home/users/nenarokova/blasto/tRNAseq/p57-cyto_trimmed_vsearch_out.fasta"
db_path="/home/users/nenarokova/blasto/tRNAseq/p57-cyto_trimmed_vsearch_out.dmnd"
threads="40"
outfile="/home/users/nenarokova/myxo/smol_diamond_nr_normal.tsv"

diamond makedb --in $fasta --db $db_path --threads $threads

diamond blastn -q $fasta -d $db_path -o $outfile -f 6 -p $threads --sensitive
