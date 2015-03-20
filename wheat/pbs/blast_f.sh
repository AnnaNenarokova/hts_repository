#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
cd /home/nenarokova/ngs/wheat/
python blast_fastq.py