#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=1


f="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_mapped.1.fq.gz"
/home/nenarokova/tools/FastQC/fastqc $f &

f="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/hiseq_mapped.2.fq.gz"
/home/nenarokova/tools/FastQC/fastqc $f &

f="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_mapped.1.fq.gz"
/home/nenarokova/tools/FastQC/fastqc $f &

f="/home/nenarokova/genomes/novymonas/assembly/pnov_submission/miseq_mapped.2.fq.gz"
/home/nenarokova/tools/FastQC/fastqc $f &
