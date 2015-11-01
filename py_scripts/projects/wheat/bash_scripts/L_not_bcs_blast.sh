#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
adapter='/mnt/lustre/nenarokova/ngs/wheat/right_barcodes_adaptered.fasta'
outfile='/mnt/lustre/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/not_bsc/not_bsc_1_blast_right_bsc.csv'
blast_db='/mnt/lustre/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/not_bsc/not_bsc_1/db_folder/not_bsc_1.db'
blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short -num_threads 24