#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
cd /mnt/lustre/nenarokova/wheat/
makeblastdb -in R1_not_bsc_1.fasta -parse_seqids -dbtype nucl -out R1_not_bsc_1.db
