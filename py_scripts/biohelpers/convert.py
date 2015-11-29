#!/usr/bin/python
from Bio.SeqIO import convert
def fastq_fasta(fastq_file):
	fasta_file = fastq_file[0:-1] + 'a'
	convert(fastq_file, "fastq", fasta_file, "fasta")
	return fasta_file