#!/usr/bin/python
from Bio import SeqIO

l = [
"NODE_98438_length_2364_cov_805.717",
"NODE_78410_length_20700_cov_930.266",
"NODE_54685_length_2424_cov_883.647",
"NODE_90282_length_848_cov_754.927"
]

# fasta = '/home/anna/bioinformatics/blasto/jaculum/jaculum_before_rr.fasta'
# results = []

# for record in SeqIO.parse(fasta, "fasta"):
#     if record.id in l:
#         results.append(record)

# outpath = '/home/anna/bioinformatics/blasto/jaculum/jaculum_kinetoplast.fasta'

# SeqIO.write(results, outpath, "fasta")

n = 3000
fasta = '/home/anna/bioinformatics/blasto/jaculum/jaculum_scaffolds.fasta'
results = []
i = 0
for record in SeqIO.parse(fasta, "fasta"):
    if i < n:
        results.append(record)
    i+=1

outpath = '/home/anna/bioinformatics/blasto/jaculum/jaculum_first3000.fasta'

SeqIO.write(results, outpath, "fasta")
