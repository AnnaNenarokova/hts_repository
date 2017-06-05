#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/insertions/alignments/ins_p57_nt.fasta', 'fasta')
outfile = open('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/insertions/alignments/ins_p57_GC.tsv', 'w')

outfile.write('{}\t{}\t{}\t{}\t{}\n'.format('sequence', 'sequence length [# nt]', 'GC content [%]', 
	'AT content [%]', 'ambiguous [# nt]'))

def GC_calculator(sequence):
	ambiguous = 0
	T = sequence.count('T')
	A = sequence.count('A')
	C = sequence.count('C')
	G = sequence.count('G')
	for i in sequence:
		if i not in 'TACG':
			ambiguous += 1
	if (G+C+A+T) != 0:
		GC_content = round((G+C)*100/(G+C+A+T), 2)
		AT_content = 100 - GC_content
	else:
		GC_content = 'NA'
		AT_content = 'NA'
	return GC_content, AT_content, ambiguous

for sequence in infile:
	seq = sequence.seq.upper()
	name = sequence.name
	outfile.write('{}\t{}\t{}\t{}\t{}\n'.format(name, len(seq), GC_calculator(seq)[0], 
		GC_calculator(seq)[1], GC_calculator(seq)[2]))
outfile.close()