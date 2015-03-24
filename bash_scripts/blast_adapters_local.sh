#!/bin/bash
cd /home/anna/bioinformatics/wheat/blast_db
blastn -query /home/anna/bioinformatics/wheat/adapters.fa -out /home/anna/bioinformatics/wheat/H7_1.out -outfmt 10 -db H7_1.db -task blastn-short 