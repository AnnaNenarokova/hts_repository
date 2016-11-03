#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

bt2_base='/home/nenarokova/genomes/hinxton_species/contaminants/genomes/leptomonas'

fw_paired="/home/nenarokova/genomes/novymonas/raw_illumina/E262_1.fastq.gz"
rv_paired="/home/nenarokova/genomes/novymonas/raw_illumina/E262_2.fastq.gz"

alignment="/home/nenarokova/genomes/novymonas/mapping/l_pyrrhocoris/l_pyrrhocoris.sam"
report="/home/nenarokova/genomes/novymonas/mapping/l_pyrrhocoris/l_pyrrhocoris_bw2_stats.txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $bt2_base -1 $fw_paired -2 $rv_paired  -S $alignment 2> $report
