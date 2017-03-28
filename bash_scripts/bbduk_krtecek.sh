#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=krtecek2.local:ppn=30
in1="/home/nenarokova/genomes/jaculum/reads/1_1.fastq.gz"
in2="/home/nenarokova/genomes/jaculum/reads/1_2.fastq.gz"
out1="/home/nenarokova/genomes/jaculum/reads/1_1_trimmed.fastq.gz"
out2="/home/nenarokova/genomes/jaculum/reads/1_2_trimmed.fastq.gz"
/home/nenarokova/tools/bbmap/bbduk.sh in1=$in1 in2=$in2 out1=$out1 out2=$out2 qtrim=r trimq=20 overwrite=true
