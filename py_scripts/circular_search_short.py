#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/tara/')
contigs = SeqIO.parse('CENJ01.fasta', 'fasta')
circular = open('circular_CENJ01.fa', 'w')
repeats_out = open('repeats_CENJ01.fa', 'w')

for contig in contigs:
	print(contig.description)
	#search for the beginning repeat at the end of the conting
	for i in range(len(contig.seq)):
		if contig.seq.count(contig.seq[0:i+1]) > 1:
			repeat = str(contig.seq[0:i+1])
		i += 1
	if len(repeat) >= 8 and repeat == contig.seq[-len(repeat):]:
		repeats_out.write('>{}_TR@{}\n{}\n'.format(contig.description, repeat, 
			contig.seq[int(len(contig.seq)/2):]))
		circular.write('>{}\n{}\n'.format(contig.description, contig.seq))

circular.close()
repeats_out.close()