#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30
#PBS -d.
cd /home/nenarokova/contaminants/genomes
bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
$bw2_dir'bowtie2-build' --threads 30 Leptomonas_seymouri.fa seymouri
