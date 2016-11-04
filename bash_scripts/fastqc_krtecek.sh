#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30

f="/home/nenarokova/genomes/novymonas/raw_illumina/WT_MiSeq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_1P.fq"

/home/nenarokova/tools/FastQC/fastqc $f --threads 30

