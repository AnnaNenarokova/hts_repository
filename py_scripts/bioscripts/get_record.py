#!/usr/bin/python
from Bio import SeqIO

record_id = 'NODE_7_length_201686_cov_83.0068'
# start=2543
# end=2758

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/blasto/p57_scaffolds.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/PhD/bioinformatics/blasto/p57_eIF3j_contig.fa'

SeqIO.write(result, outpath, "fasta")

