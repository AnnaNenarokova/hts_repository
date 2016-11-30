#!/usr/bin/python
from Bio import SeqIO

l = [
"utg000195l|quiver|quiver|quiver",
"utg000069l|quiver|quiver|quiver"
]

fasta = '/home/anna/bioinformatics/trypanoplasma/pacbio_consensus_quiver3.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/bioinformatics/trypanoplasma/megacircle.fa'

SeqIO.write(results, outpath, "fasta")
