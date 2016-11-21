#!/usr/bin/python
from Bio import SeqIO

min_cov=3
inpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/azi_scaffolds.fa'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if float(record.id.split("_")[-1]) > min_cov:
		results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/azi_scaffolds_cov>3.fa'
SeqIO.write(results, outpath, "fasta")
