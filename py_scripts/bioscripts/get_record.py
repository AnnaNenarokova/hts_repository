#!/usr/bin/python
from Bio import SeqIO

record_id = 'NODE_1075_length_388462_cov_71.249306'

fasta_file = '/home/anna/Dropbox/phd/bioinformatics/genomes/kinetoplastids/CLC_assemblies/E262_contigs.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/phd/bioinformatics/genomes/kinetoplastids/novymonas/polished_assembly/pandorea_novymonas_contig.fasta'

SeqIO.write(result, outpath, "fasta")
