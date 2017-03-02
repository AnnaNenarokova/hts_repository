#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/Dropbox/! Data/cell_47_SPAdes-scaffolds.final.fasta', 'fasta')
output = open('/home/kika/Dropbox/! Data/cell_47_SPAdes-scaffolds_renamed.final.fasta', 'w')

for sequence in infile:
	name = sequence.description
	seq = sequence.seq
	output.write('>cell_47_{}\n{}\n'.format(name, seq))
output.close()