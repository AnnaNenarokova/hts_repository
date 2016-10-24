#!/usr/bin/python
from Bio import SeqIO

record_id = 'unitig_200|quiver'

fasta_file = '/home/anna/bioinformatics/phd/Mbr04_Wallacemonas_polished_assembly.fasta'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/bioinformatics/phd/unitig_200|quiver_walla.fasta'

SeqIO.write(result, outpath, "fasta")

