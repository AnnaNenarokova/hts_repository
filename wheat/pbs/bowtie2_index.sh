#!/bin/bash
#PBS -l nodes=1:ppn=5
#PBS -l walltime=100:00:00
#PBS -l mem=20gb

cd /home/nenarokova/wheat/wheat_bowtie2_index/
bowtie2-build /mnt/lustre/nenarokova/wheat/wheat_scaffolds.fasta wheat
