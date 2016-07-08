#!/usr/bin/python
from Bio import SeqIO

l = ['EG_transcript_8095', 'EG_transcript_4309', 'EG_transcript_8319', 'EG_transcript_4177']
fasta = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    for id in l:
        if id == record.id:
            results.append(record)

outpath = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_gracilis_fts_transcripts.fasta'

SeqIO.write(results, outpath, "fasta")
