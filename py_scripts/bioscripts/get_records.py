#!/usr/bin/python
from Bio import SeqIO

l = [
'TRINITY_GG_1521_c0_g2_i1_4',
'TRINITY_GG_1521_c0_g1_i1_6'
]

fasta = '/home/anna/Dropbox/PhD/bioinformatics/blasto/transcriptome/Trinity-GG_p57_6_frames_translated.faa'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/blasto/transcriptome/trp_trna_sythases.faa'

SeqIO.write(results, outpath, "fasta")
