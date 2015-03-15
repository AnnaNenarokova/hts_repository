#!/usr/bin/python
from Bio import SeqIO
file_fastq = '/mnt/lustre/nenarokova/wheat/R1/sum_fastq1/not_bsc_1.fastq'
file_fasta = '/mnt/lustre/nenarokova/wheat/R1_not_bsc_1.fasta'
SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")
