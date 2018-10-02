#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_path = ""
outpath = ""
records = []

for record in SeqIO.parse(fasta_path, "fasta"):
    records.append(record)

results = []

SeqIO.write(results, open(outpath, 'w'), "fasta")
