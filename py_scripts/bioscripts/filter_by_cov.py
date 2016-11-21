#!/usr/bin/python
from Bio import SeqIO

min_cov=10
inpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/azi_scaffolds.fa'
results = []

for record in SeqIO.parse(inpath, "fasta"):
    if float(record.id.split("_")[-1]) > min_cov:
		results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/azi_scaffolds_cov>10.fa'
SeqIO.write(results, outpath, "fasta")
