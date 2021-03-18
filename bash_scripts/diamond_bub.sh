#!/bin/bash

threads="96"
diamond="/home/software/diamond"
refdb_folder="/mnt/data/metagenomic_data/ref_blast/ref_db/"
out_folder="/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/"

query1="/mnt/data/metagenomic_data/spades_runs/K26/contigs.fasta"
out1=$out_folder"K26_"
query2="/mnt/data/metagenomic_data/spades_runs/SpadesK28_Hippobosca/contigs.fasta"
out2=$out_folder"K28_"
custom_outfmt="6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"

cd $refdb_folder
for f in *.faa
do
    $diamond makedb --in $f -d $f
    db=$f".dmnd"
    $diamond blastx -q $query1 -d $db -o $out1$db".tsv" -f $custom_outfmt -p $threads
    $diamond blastx -q $query2 -d $db -o $out2$db".tsv" -f $custom_outfmt -p $threads
done
