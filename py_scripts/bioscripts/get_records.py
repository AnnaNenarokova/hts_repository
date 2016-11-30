#!/usr/bin/python
from Bio import SeqIO

l = [
"NODE_360_length_5590_cov_27.5437",
"NODE_653_length_1849_cov_366.961"
]

fasta = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/wt_spades/wt_scaffolds.fa'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/wt_spades/suspicious.fa'

SeqIO.write(results, outpath, "fasta")
