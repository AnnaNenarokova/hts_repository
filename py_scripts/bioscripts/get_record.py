#!/usr/bin/python
from Bio import SeqIO

record_id = 'NODE_822_length_1318_cov_1863.76'

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/wt_scaffolds.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/pandorea_sc_822.fa'

SeqIO.write(result, outpath, "fasta")

