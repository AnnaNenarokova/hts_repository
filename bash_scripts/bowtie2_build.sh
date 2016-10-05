#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60
#PBS -d.
cd /home/nenarokova/genomes/kinetoplastids/pacbio/assembly
bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
$bw2_dir'bowtie2-build' --threads 60 Mbr04_Wallacemonas_polished_assembly.fasta wallacemonas
$bw2_dir'bowtie2-build' --threads 60 PNG-M02_Aambiguus_polished_assembly.fasta angomonas
