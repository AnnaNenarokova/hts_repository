#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
cd /home/nenarokova/wheat
blastn -query ./wheat_adapter.fasta -subject ./R1.fasta -out ./not_bcs_1_report -outfmt 10
