#!/usr/bin/python
from Bio import SeqIO

record_id = 'unitig_0|quiver'

fasta_file = '/home/anna/Dropbox/phd/bioinformatics/genomes/kinetoplastids/novymonas/e262_polished_pacbio_assembly.fasta'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/phd/bioinformatics/genomes/kinetoplastids/novymonas/novymonas_contig_pacbio.fasta'

SeqIO.write(result, outpath, "fasta")
