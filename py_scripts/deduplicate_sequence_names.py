#!/usr/bin/python3
from Bio import SeqIO
from collections import OrderedDict

infile = SeqIO.parse('/home/kika/Dropbox/PABP.fa', 'fasta')
output = open('/home/kika/Dropbox/PABP_dedupl.fa', 'w')

seq_dict = OrderedDict()
for sequence in infile:
	seq_dict[sequence.description] = sequence.seq

for key, value in seq_dict.items():
	output.write('>{}\n{}\n'.format(key, value))
output.close()