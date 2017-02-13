#!/usr/bin/python
from Bio import SeqIO

record_id = 'NODE_7_length_201686_cov_83.0068_3'
start=2543
end=2758

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/blasto/p57_DNA_translated.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record[start:end]
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/PhD/bioinformatics/blasto/p57_eIF3j.fa'

SeqIO.write(result, outpath, "fasta")

