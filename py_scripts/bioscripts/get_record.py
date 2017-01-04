#!/usr/bin/python
from Bio import SeqIO

record_id = 'NODE_6258_length_1665_cov_2.55155'

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/blasto_kika/scaffolds_triat.fasta'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/blasto_kika/NODE_6258_length_1665_cov_2_55155.fasta'

SeqIO.write(result, outpath, "fasta")

