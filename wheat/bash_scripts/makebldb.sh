#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
makeblastdb -in /home/anna/bioinformatics/htses/ERR015599/not_bsc_1/not_bsc_1.fasta -parse_seqids -dbtype nucl -out /home/anna/bioinformatics/htses/ERR015599/not_bsc_1/blast_db/not_bsc_1.db
