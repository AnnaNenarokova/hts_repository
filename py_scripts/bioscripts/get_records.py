#!/usr/bin/python
from Bio import SeqIO

l = [
"TRINITY_GG_1794_c0_g1_i1",
"TRINITY_GG_1794_c0_g2_i1"
]

fasta = '/home/anna/bioinformatics/blasto/p57_trinity.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/bioinformatics/blasto/p57_RNA_helicase_transcript.fa'

SeqIO.write(results, outpath, "fasta")
