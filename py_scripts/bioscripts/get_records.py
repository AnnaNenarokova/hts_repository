#!/usr/bin/python
from Bio import SeqIO

l = [
"EG_transcript_18355",
"EG_transcript_20320"
]

fasta = '/media/anna/data/Dropbox/PhD/projects/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/media/anna/data/Dropbox/PhD/projects/euglena/data/hassan.fasta'

SeqIO.write(results, outpath, "fasta")
