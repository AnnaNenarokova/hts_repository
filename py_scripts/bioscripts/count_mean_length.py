#!/usr/bin/python
from Bio import SeqIO
import sys

fasta_file = sys.argv[1]

n_seq = 0
total_len = 0
for record in SeqIO.parse(fasta_file, "fasta"):
    n_seq += 1
    total_len += len(record.seq)
print fasta_file
print total_len/float(n_seq)



