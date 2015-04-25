#!/usr/bin/python
from Bio import SeqIO
fastq_file = '/home/anna/bioinformatics/'
for seq_record in SeqIO.parse(fasta_file, "fastq"):
	