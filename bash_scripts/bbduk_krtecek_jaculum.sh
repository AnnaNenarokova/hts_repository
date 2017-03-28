#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=krtecek2.local:ppn=64
in1="/home/nenarokova/genomes/jaculum/reads/1_1.fastq.gz"
in2="/home/nenarokova/genomes/jaculum/reads/1_2.fastq.gz"
out1="/home/nenarokova/genomes/jaculum/reads/1_1_trimmed.fastq.gz"
out2="/home/nenarokova/genomes/jaculum/reads/1_2_trimmed.fastq.gz"
err_out="/home/nenarokova/genomes/jaculum/reads/err.txt"
adapters="/home/nenarokova/tools/bbmap/resources/adapters.fa"
/home/nenarokova/tools/bbmap/bbduk.sh overwrite=true in1=$in1 in2=$in2 out1=$out1 out2=$out2 ref=$adapters ktrim=r k=22 mink=11 hdist=2 tpe tbo t=64 qtrim=rl trimq=20
