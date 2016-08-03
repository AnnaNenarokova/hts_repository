#!/usr/bin/python
from Bio import SeqIO

l = ['TR13625|c0_g3_i1', 'TR13625|c0_g2_i1']
fasta = '/home/anna/Dropbox/phd/bioinformatics/genomes/hemistasia/Hemistasia_cutadapt_trinity_run3.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    for id in l:
        if id == record.id:
            results.append(record)

outpath = '/home/anna/Dropbox/phd/bioinformatics/genomes/hemistasia/Hemistasia_histidine_phospatases.fasta'

SeqIO.write(results, outpath, "fasta")
