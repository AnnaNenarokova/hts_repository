#!/bin/bash
#PBS -l nodes=1:ppn=5
#PBS -l walltime=100:00:00
#PBS -l mem=10gb
adapter='/mnt/lustre/nenarokova/ngs/wheat/right_barcodes.fasta'
outfile='/mnt/lustre/nenarokova/wheat/R1_not_bc_right_bsc.csv'
blast_db='/mnt/lustre/nenarokova/wheat/R1_not_bsc_bl_db/R1_not_bsc_1.db'
blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short -num_threads 24