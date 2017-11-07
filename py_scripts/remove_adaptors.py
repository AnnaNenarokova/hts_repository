#!/usr/bin/python3
import os
import re
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/paratrypanosoma/')
contamination = open('contamination.txt', 'r')
contigs = SeqIO.parse('Paratrypanosoma_genome_final_PE_MP_Newbler_500bp_up.fa', 'fasta')
gff_file = open('test.gff', 'r')
contigs_upd = open('paratryp_new.fa', 'w')
new_gff = open('paratryp_new.gff', 'w')

def get_coordinates(contamination):
	adaptors = {}
	for row in contamination:
		if ',' in row.split('\t')[2]:
			for item in row.split('\t')[2].split(','):
				beginning = int(item.split('..')[0])
				end = int(item.split('..')[1])
				whole = [beginning, end]
				if row.split('\t')[0] not in adaptors:
					adaptors[row.split('\t')[0]] = [whole]
				else:
					adaptors[row.split('\t')[0]].append(whole)
		else:
			beginning = int(row.split('\t')[2].split('..')[0])
			end = int(row.split('\t')[2].split('..')[1])
			whole = [beginning, end]
			adaptors[row.split('\t')[0]] = [whole]
	return adaptors
	# contig name : [[start, end], [start,end]]
	# 				   adaptor1		 adaptor2

def gff(gff_file):
	ids = OrderedDict()
	lines_after_2 = gff_file.readlines()[2:]
	for row in lines_after_2:
		seqid = row.split('\t')[0]
		source = row.split('\t')[1]
		ftype = row.split('\t')[2]
		start = int(row.split('\t')[3])
		end = int(row.split('\t')[4])
		score = str(row.split('\t')[5])
		strand = row.split('\t')[6]
		phase = int(row.split('\t')[7])
		attributes = row.split('\t')[8][:-1]
		ids[seqid] = [source, ftype, start, end, score, strand, phase, attributes]
	return ids

adaptors = get_coordinates(contamination)
ids = gff(gff_file)
remove = ['contig06599', 'scaffold00124']

genome = OrderedDict()
for contig in contigs:
	for key, value in adaptors.items():
		if contig.description == key:
			if len(value) == 1:
				for i in value:
					if i[0] == 1:
						genome[key] = contig.seq[i[1]:]
					elif i[1] == len(contig.seq):
						genome[key] = contig.seq[:i[0]-1]
					else:
						genome[key + '_1'] = contig.seq[:(i[0]-1)]
						genome[key + '_2'] = contig.seq[i[1]:]
			else:
				if value[0][0] == 1 and value[-1][1] == len(contig.seq):
					genome[key] = contig.seq[value[0][1]:value[-1][0]-1]
				else:
					genome[key + '_1'] = contig.seq[:value[0][0]-1]
					c = 1
					while c <= len(value):
						try:
							genome[key + '_' + str(c+1)] = contig.seq[value[c-1][1]:value[c][0]-1]
						except IndexError:
							genome[key + '_' + str(c+1)] = contig.seq[value[-1][1]:]
						c += 1
		elif contig.description in remove:
			pass
		else:
			if contig.description in genome:
				pass
			else:
				genome[contig.description] = contig.seq

for key, value in genome.items():
	contigs_upd.write('>{}\n{}\n'.format(key, value))


new_gff.write('##gff-version 3\n')
new_gff.write('##Augustus predicted 7982 genes\n')

for key, value in ids.items():
	for ak, av in adaptors.items():
		if key == ak:
			if len(av) == 1:
				for i in av:
					if i[0] == 1 and value[2] == 1:
						value[3] = value[3] - i[1]
						new_gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], 
							value[2], value[3], value[4], value[5], value[6], value[7]))
					elif i[0] == 1 and i[1] > value[2]:
						dif = value[2] - i[0]
						value[2] = 1
						value[3] = value[3] - (i[1] - i[0]) - dif + 1
						new_gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], 
							value[2], value[3], value[4], value[5], value[6], value[7]))
					elif i[0] == 1 and i[1] < value[2]:
						value[2] = value[2] - i[1]
						value[3] = value[3] - i[1]
						new_gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], 
							value[2], value[3], value[4], value[5], value[6], value[7]))
					elif i[0] < value[3] and i[1] >= value[3]:
						value[3] == i[0] - 1
						new_gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], 
								value[2], value[3], value[4], value[5], value[6], value[7]))
					elif i[0] > value[3]:
						new_gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], 
								value[2], value[3], value[4], value[5], value[6], value[7]))
					#just 1 adaptor in the middle of sequence
			#several adaptors in the sequence
		# elif key in remove:
			# pass
		# else:
			# new_gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(key, value[0], value[1], value[2], 
				# value[3], value[4], value[5], value[6], value[7]))

contigs_upd.close()
new_gff.close()