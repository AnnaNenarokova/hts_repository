#!/bin/bash
cd /home/anna/bioinformatics/tools/blasto
csv="/home/anna/bioinformatics/all_proteome_references_bl_reports/Blechomonas_ayalai_aa.fasta_bl_report.csv"
./bin/blast_to_gff.rb -in $csv -t subject -b -m spades --extend --show_extended --merge --show_merged
