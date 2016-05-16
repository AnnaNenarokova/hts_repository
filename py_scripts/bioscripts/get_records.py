#!/usr/bin/python
from Bio import SeqIO

fasta = '/home/anna/Dropbox/phd/kinetoplastids/wallacemonas_polished_assembly_hgap.fasta'
i = 0
for record in SeqIO.parse(f, "fasta"):
    if i%5000 == 0:
        k = 0

    i+=1
outpath = '/home/anna/Dropbox/phd/kinetoplastids/wallacemonas_first_contig.fasta'

SeqIO.write(result, outpath, "fasta")
