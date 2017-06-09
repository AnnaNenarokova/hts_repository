#!/usr/bin/python
from Bio import SeqIO

l = [
"TR84023|c0_g1_i2|m.16885",
"TR101069|c0_g1_i1|m.22182",
"TR22120|c0_g1_i1|m.2431",
"TR59486|c0_g1_i1|m.8773"

]

fasta = '/media/anna/data/Dropbox/PhD/projects/diplonema/Proteins_and_Transcripts_201604/proteins_SL.faa'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/media/anna/data/Dropbox/PhD/projects/diplonema/Proteins_and_Transcripts_201604/HR_diplonema.faa'

SeqIO.write(results, outpath, "fasta")

# n = 3000
# fasta = '/home/anna/bioinformatics/blasto/jaculum/jaculum_scaffolds.fasta'
# results = []
# i = 0
# for record in SeqIO.parse(fasta, "fasta"):
#     if i < n:
#         results.append(record)
#     i+=1

# outpath = '/home/anna/bioinformatics/blasto/jaculum/jaculum_first3000.fasta'

# SeqIO.write(results, outpath, "fasta")
