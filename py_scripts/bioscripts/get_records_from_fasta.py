#!/usr/bin/python
from Bio import SeqIO


l = ["EG_transcript_13141", "EG_transcript_24338", "EG_transcript_3434", "EG_transcript_559", "EG_transcript_6397", "EG_transcript_8044"]
fasta = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_all_proteins.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    for id in l:
        if id == record.id:
            results.append(record)

outpath = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_proteins_SufCB.fasta'

SeqIO.write(results, outpath, "fasta")
