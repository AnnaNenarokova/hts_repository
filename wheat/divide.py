#!/usr/bin/python
import csv
from Bio import SeqIO
fasta_file = ''
for seq_record in SeqIO.parse(fasta_file, "fasta"):