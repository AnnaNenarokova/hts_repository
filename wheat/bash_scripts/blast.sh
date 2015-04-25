#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
blast_db='/mnt/lustre/nenarokova/wheat/new_assembly_blastdb/wheat_scaffolds.db'
# fasta='/mnt/lustre/nenarokova/wheat/NBS_LRR_all_plants.fasta'
fasta='/home/anna/bioinformatics/ngs/wheat/Cocos_nucifera_RGA.fasta'
outfile='/home/nenarokova/wheat/NBS_LRR_new_assembly_blreport'
blastn -query $fasta -db $blast_db -out $outfile -outfmt 10 -num_threads 24
	