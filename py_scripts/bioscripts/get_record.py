#!/usr/bin/python
from Bio import SeqIO

record_id = 'utg000035l|quiver|quiver|quiver'

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanoplasma/pacbio_consensus_quiver3.fasta'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanoplasma/kinetoplast.fasta'

SeqIO.write(result, outpath, "fasta")

