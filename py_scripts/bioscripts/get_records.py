#!/usr/bin/python
from Bio import SeqIO

l = ['EG_transcript_12368',
'EG_transcript_11734',
'EG_transcript_30166',
'EG_transcript_19555',
'EG_transcript_31130',
'EG_transcript_16635',
'EG_transcript_33996',
'EG_transcript_10631',
'EG_transcript_8016',
'EG_transcript_25719',
'EG_transcript_8552']
fasta = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_all_proteins.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    for id in l:
        if id == record.id:
            results.append(record)

outpath = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_import.fasta'

SeqIO.write(results, outpath, "fasta")
