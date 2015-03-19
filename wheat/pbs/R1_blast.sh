#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
adapter='/mnt/lustre/nenarokova/wheat/universal_adapter.fasta'
outfile='/mnt/lustre/nenarokova/wheat/R1_blast_out.csv'
blast_db='/mnt/lustre/nenarokova/wheat/R1_not_bsc_bl_db/R1_not_bsc_1.db'
blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short num_threads 24