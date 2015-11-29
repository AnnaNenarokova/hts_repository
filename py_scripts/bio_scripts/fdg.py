#!/usr/bin/python
from Bio import SeqIO
f = '/home/anna/bioinformatics/euglenozoa/euglena/Euglena_gracilis_genome_V1.fasta'
file_out = '/home/anna/bioinformatics/euglenozoa/euglena/Euglena_100_contigs.fasta'
i = 0
out = []
for record in SeqIO.parse(f, "fasta"):
	out.append(record)
	i+=1
	if i==100: break

SeqIO.write(out, file_out, "fasta")