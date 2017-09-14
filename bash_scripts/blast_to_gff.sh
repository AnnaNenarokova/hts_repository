#!/bin/bash
cd /home/anna/bioinformatics/tools/blasto
csv="/home/anna/bioinformatics/igv_sessions/jaculum_igv/kinetoplastid_proteoms.fasta_bl_report_best.csv"
./bin/blast_to_gff.rb -in $csv -t subject -b -m spades --extend --show_extended
