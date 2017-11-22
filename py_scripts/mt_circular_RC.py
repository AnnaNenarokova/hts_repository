#!/usr/bin/python3
import os
import subprocess
from Bio import SeqIO

os.chdir('/home/kika/tara/')
contigs = SeqIO.parse('CENF01.fasta', 'fasta')
circular = open('circular_RC.fa', 'w')
candidates = open('candidates_RC.fa', 'w')
non_circ = open('non_circular_RC.fa', 'w')
short_long = open('short_long_RC.fa', 'w')
repeats_out = open('repeats_RC.fa', 'w')

print('Searching for repeats in sequences')

cand_dict = {}
circ_dict = {}
nc_dict = {}
for contig in contigs:
	print(contig.description)
	#search for the beginning repeat at the end of the conting
	for i in range(len(contig.seq)):
		if contig.seq.count(contig.seq[0:i+1]) > 1:
			repeat = str(contig.seq[0:i+1])
		i += 1
	if len(repeat) >= 8 and repeat == contig.seq[-len(repeat):]:
		circ_dict[contig.description] = contig.seq
		repeats_out.write('>{}_TR@{}\n{}\n'.format(contig.description, repeat, 
			contig.seq[int(len(contig.seq)/2):]))

	if contig.description not in circ_dict:
		if len(contig.seq) > 15000 and len(contig.seq) < 100000:
			#search for the beginning repeat longer than 15bp and present in the second half of the contig
			for i in range(len(contig.seq)):
				if contig.seq.count(contig.seq[0:i+1]) > 1:
					repeat = str(contig.seq[0:i+1])
				i += 1
			if len(repeat) >= 15 and repeat in contig.seq[int(len(contig.seq)/2):]:
				cand_dict[contig.description] = contig.seq
				repeats_out.write('>{}_BR@{}\n{}\n'.format(contig.description, repeat, 
					contig.seq[int(len(contig.seq)/2):]))
			#search for the last repeat longer than 15bp and present in the first half of the contig
			else:
				reverse = contig.seq.reverse_complement()
				for i in range(len(reverse)):
					if reverse.count(reverse[0:i+1]) > 1:
						repeat = str(reverse[0:i+1])
					i += 1
				if len (repeat) >= 15 and repeat in reverse[int(len(reverse)/2):]:
					cand_dict[contig.description + '_RC'] = reverse
					repeats_out.write('>{}_LR@{}\n{}\n'.format(contig.description, repeat, 
						reverse[int(len(reverse)/2):]))

			if contig.description in cand_dict:
				pass
			else:
				nc_dict[contig.description] = contig.seq
		else:
			short_long.write('>{}\n{}\n'.format(contig.description, contig.seq))

for key, value in cand_dict.items():
	candidates.write('>{}\n{}\n'.format(key, value))
for key, value in circ_dict.items():
	circular.write('>{}\n{}\n'.format(key, value))
for key, value in nc_dict.items():
	non_circ.write('>{}\n{}\n'.format(key, value))

circular.close()
candidates.close()
non_circ.close()
short_long.close()
repeats_out.close()