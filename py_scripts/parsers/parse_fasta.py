#!/usr/bin/python
from Bio import SeqIO
fasta_file = '/home/anna/bioinformatics/outdirs/IS_BL21.fasta'
for seq_record in SeqIO.parse(fasta_file, "fasta"):
	
fastq_file = '/home/anna/bioinformatics/'
for seq_record in SeqIO.parse(fasta_file, "fastq"):
	