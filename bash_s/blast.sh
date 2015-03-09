#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/anna/bioinformatics/
blastn -query wheat_adapter.fasta -subject adapters.fa -out not_bcs_1_report -outfmt 10 -num_threads 8
