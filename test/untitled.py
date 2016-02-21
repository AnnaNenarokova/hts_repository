#!/usr/bin/python
from Bio import SeqIO

fasta_path = '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.fasta'
i = 0
for record in SeqIO.parse(fasta_path, "fasta"):
    i+=1

print i