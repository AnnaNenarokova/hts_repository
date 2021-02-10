#!/usr/bin/python
from Bio import SeqIO

min_cov=5
inpath = '/Users/annanenarokova/Google Drive/projects/novymonas/novymonas/genome/novymonas_no_pand_scaffolds.fasta'
results = []

for record in SeqIO.parse(inpath, "fasta"):
    if float(record.id.split("_")[-1]) > min_cov and len(record) > 200:
        results.append(record)

outpath = '/Users/annanenarokova/Google Drive/projects/novymonas/novymonas/genome/novymonas_filtered_for_genbank.fasta'
SeqIO.write(results, outpath, "fasta")
