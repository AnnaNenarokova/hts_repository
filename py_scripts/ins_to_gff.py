#!/usr/bin/python3
#!!! check parsing file name in the full_prot fuction !!!
import os
import re
from Bio import SeqIO, AlignIO
from collections import OrderedDict, defaultdict

os.chdir('/home/kika/alignments/')
files = os.listdir()
p57_nt = open('p57_nt.txt', 'w')
p57_aa = open('p57_aa.txt', 'w')
triat_aa = open('triat_aa.txt', 'w')
bexlh_aa = open('bexlh_aa.txt', 'w')
jac_aa = open('jac_aa.txt', 'w')
gff = open('p57_insertions.gff', 'w')
errors = open('p57_errors.txt', 'w')
genome = '/home/kika/programs/blast-2.5.0+/bin/p57_DNA_scaffolds.fa'
gencode = {
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'X', 'TAG':'X',
	'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}

gff.write('{}\t{}\n'.format('##gff-version', '3'))

def get_seq_number(aln_file):
	sequences = SeqIO.parse(aln_file, 'fasta')
	number = 0
	p57_triat_BexLH_jac = [None, None, None, None]
	for sequence in sequences:
		if ('p57' not in sequence.name and 'triat' not in sequence.name and 
			'BexLH' not in sequence.name and 'jac' not in sequence.name):  
			number += 1
		elif 'p57' in sequence.name:
			p57_triat_BexLH_jac[0] = number
			number += 1
		elif 'triat' in sequence.name:
			p57_triat_BexLH_jac[1] = number
			number += 1
		elif 'BexLH' in sequence.name:
			p57_triat_BexLH_jac[2] = number
			number += 1
		elif 'jac' in sequence.name:
			p57_triat_BexLH_jac[3] = number
			number += 1
	return p57_triat_BexLH_jac

def find_insertion(aln_file):
	alignment = AlignIO.read(aln_file, 'fasta')
	seq_numbers = get_seq_number(aln_file)
	seqs_present = []
	result_list = []
	for number in seq_numbers:
		if number != None:
			seqs_present.append(number)
	for i in range(alignment.get_alignment_length()):
		column = alignment.get_column(i)
		dash_count = column.count('-')
		if dash_count >= len(alignment) - len(seqs_present):
			true_insertions = 0
			for seq in seqs_present:
				if column[seq] != '-':
					true_insertions += 1
			if true_insertions + dash_count == len(alignment):
				column_list = list(column)
				column_list.append(i)
				result_list.append(column_list)
	return result_list

def get_peptides(table, aln_file):
	alignment = AlignIO.read(aln_file, 'fasta')
	seq_numbers = get_seq_number(aln_file)
	p57 = []
	triat = []
	bexlh = []
	jac = []
	for number in seq_numbers:
		peptide = ''
		column_number = 0
		if number != None:
			seq_index = int(seq_numbers.index(number))
			for i in range(len(table)):
			#list of lists(columns with hits, last item is column number)
				if int(i) == int(len(table)) - 1:
					peptide += table[i][seq_numbers[seq_index]]
					if seq_index == 0:
						p57.append(peptide.replace('-', ''))
					elif seq_index == 1:
						triat.append(peptide.replace('-', ''))
					elif seq_index == 2:
						bexlh.append(peptide.replace('-', ''))
					elif seq_index == 3:
						jac.append(peptide.replace('-', ''))
				elif table[i][seq_numbers[seq_index]] != '-' and len(peptide) < 1:
					peptide = table[i][seq_numbers[seq_index]]
					column_number = int(table[i][-1])
				elif int(table[i][-1]) == column_number + 1:
					peptide += table[i][seq_numbers[seq_index]]
					column_number = int(table[i][-1])
				elif table[i][seq_numbers[seq_index]] != '-' and (int(table[i][-1]) != column_number + 1):
					if seq_index == 0:
						p57.append(peptide.replace('-', ''))
					elif seq_index == 1:
						triat.append(peptide.replace('-', ''))
					elif seq_index == 2:
						bexlh.append(peptide.replace('-', ''))
					elif seq_index == 3:
						jac.append(peptide.replace('-', ''))
					peptide = table[i][seq_numbers[seq_index]]
					column_number = int(table[i][-1])
			if seq_index == 0:
				for seq in alignment:
					if 'p57' in seq.name:
						count = 0
						for i in p57:
							count += 1
							p57_aa.write('>{}_{}\n{}\n'.format(seq.name[4:], count, i))
							p57_aa_dict['{}_{}'.format(seq.name[4:], count)] = i
			if seq_index == 1:
				for seq in alignment:
					if 'triat' in seq.name:
						count = 0
						for i in p57:
							count += 1
							triat_aa.write('>{}_{}\n{}\n'.format(seq.name[6:], count, i))
			if seq_index == 2:
				for seq in alignment:
					if 'bexlh' in seq.name:
						count = 0
						for i in p57:
							count += 1
							bexlh_aa.write('>{}_{}\n{}\n'.format(seq.name[6:], count, i))
			if seq_index == 3:
				for seq in alignment:
					if 'jac' in seq.name:
						count = 0
						for i in p57:
							count += 1
							jac_aa.write('>{}_{}\n{}\n'.format(seq.name[4:], count, i))
	return p57_aa_dict

def full_prot(aln_file):
	alignment = AlignIO.read(aln_file, 'fasta')
	file_name = aln_file.split('.marker')[0]
	full_protein = []
	# full_prot_dict = {}
	full_prot_dict = defaultdict(list)
	for seq in alignment:
		if 'p57' in seq.name:
			name = re.search(r'NODE_\d+_length_\d+_cov_\d+.\d+', seq.name).group()
	# 		full_protein.append([name, str(seq.seq).replace('-', ''), file_name])
	# full_prot_dict[full_protein[0][0]] = (full_protein[0][1], full_protein[0][2])
			full_prot_dict[name].append(str(seq.seq).replace('-', ''))
			full_prot_dict[name].append(file_name)
	return full_prot_dict

def translation(nucl_seq):
	cut_seq = []
	for i in range(0,len(nucl_seq)-2, 3):
		cut_seq.append(nucl_seq[i:i+3])
	aa = []
	for codon in cut_seq:
		if 'N' in codon:
			aa.append('X')
		else:
			aa.append(gencode[codon])
	return ''.join(aa)

def get_full_orf(genome, proteins):
	contigs = SeqIO.parse(genome, 'fasta')
	proteins_from_aln = proteins
	p57_contigs = {}
	for contig in contigs:
		p57_contigs[contig.name] = contig.seq
	orf_nt = {}
	for key in proteins_from_aln.keys():
		key_root = re.sub(r'(NODE_\d+_length_\d+_cov_\d+.\d+)_.*', r'\g<1>', key)
		if key_root in p57_contigs.keys():
			nucl = p57_contigs[key_root]
			reverse = nucl.reverse_complement()
			prot = proteins_from_aln[key][0]
			if str(prot) in translation(nucl):
				orf_start = (translation(nucl).find(str(prot))) * 3
				orf_end = orf_start + (len(prot) * 3) + 3
				frame = '1'
				orf_nt[key_root] = [nucl[orf_start:orf_end], orf_start+1, orf_end, frame, proteins_from_aln[key][1]]
			elif str(prot) in translation(nucl[1:]):
				orf_start = 1 + (translation(nucl[1:]).find(str(prot))) * 3
				orf_end = orf_start + (len(prot) * 3) + 3
				frame = '2'
				orf_nt[key_root] = [nucl[orf_start:orf_end], orf_start+1, orf_end, frame, proteins_from_aln[key][1]]
			elif str(prot) in translation(nucl[2:]):
				orf_start = 2 + (translation(nucl[2:]).find(str(prot))) * 3
				orf_end = orf_start + (len(prot) * 3) + 3
				frame = '3'
				orf_nt[key_root] = [nucl[orf_start:orf_end], orf_start+1, orf_end, frame, proteins_from_aln[key][1]]
			elif str(prot) in translation(reverse):
				orf_start = (translation(reverse).find(str(prot))) * 3
				orf_end = orf_start + (len(prot) * 3) + 3
				orf_start_contig = len(reverse) - orf_end
				orf_end_contig = len(reverse) - orf_start
				frame = 'c1'
				orf_nt[key_root] = [reverse[orf_start:orf_end], orf_start_contig+1, orf_end_contig, frame, proteins_from_aln[key][1]]
			elif str(prot) in translation(reverse[1:]):
				orf_start = 1 + (translation(reverse[1:]).find(str(prot))) * 3
				orf_end = orf_start + (len(prot) * 3) + 3
				orf_start_contig = len(reverse) - orf_end
				orf_end_contig = len(reverse) - orf_start
				frame = 'c2'
				orf_nt[key_root] = [reverse[orf_start:orf_end], orf_start_contig+1, orf_end_contig, frame, proteins_from_aln[key][1]]
			elif str(prot) in translation(reverse[2:]):
				orf_start = 2 + (translation(reverse[2:]).find(str(prot))) * 3
				orf_end = orf_start + (len(prot) * 3) + 3
				orf_start_contig = len(reverse) - orf_end
				orf_end_contig = len(reverse) - orf_start
				frame = 'c3'
				orf_nt[key_root] = [reverse[orf_start:orf_end], orf_start_contig+1, orf_end_contig, frame, proteins_from_aln[key][1]]
	return orf_nt
	#contig name : orf sequence 	orf start 	orf_end 	frame	file name
	#			   [0]				[1]			[2]			[3]		[4]

def get_nt_ins(peptides, orf_nt):
	ins_aa = peptides
	orf_nucl = orf_nt
	ins_nt = OrderedDict()
	for key in ins_aa.keys():
		key_root = re.sub(r'(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', key)
		ins_num = re.search(r'_\d+\Z', key).group()[1:]
		if key_root in orf_nucl.keys():
			nucl = orf_nucl[key_root][0]
			prot = ins_aa[key]
			if str(prot) in translation(nucl):
				ins_start = (translation(nucl).find(str(prot))) * 3
				ins_end = ins_start + (len(prot) * 3)
				if 'c' not in orf_nucl[key_root][3]:
					ins_start_contig = orf_nucl[key_root][1] + ((translation(nucl).find(str(prot))) * 3)
					ins_end_contig = ins_start_contig + (len(prot) * 3) - 1
					ins_nt[key] = [nucl[ins_start:ins_end], ins_start_contig, ins_end_contig]
				else:
					ins_start_contig = orf_nucl[key_root][2] - ((translation(nucl).find(str(prot))) * 3)
					ins_end_contig = ins_start_contig - (len(prot) * 3) + 1
					ins_nt[key] = [nucl[ins_start:ins_end], ins_end_contig, ins_start_contig]
				p57_nt.write('>{}\n{}\n'.format(key, ins_nt[key][0]))
			else:
				errors.write('>{}\n{}\n'.format(key, ins_aa[key]))
	return ins_nt
	#contig name_ins number : 	ins sequence 	orf start 	orf_end
	#			   				[0]				[1]			[2]

all_proteins = {}
p57_aa_dict = OrderedDict()
for file in files:
	if '.aln' in file:
		print(file)
		table = find_insertion(file)
		p57_aa_dict = get_peptides(table, file)
		all_proteins = full_prot(file)
		orf_nt_dict = get_full_orf(genome, all_proteins)
		ins_nt_dict = get_nt_ins(p57_aa_dict, orf_nt_dict)
		for key in orf_nt_dict.keys():
			if 'c' in orf_nt_dict[key][3]:
				orf_line = '{}\tblast\tCDS\t{}\t{}\t1\t-\t0\tID={}\n'.format(key, orf_nt_dict[key][1], 
					orf_nt_dict[key][2], orf_nt_dict[key][4])
				for key_ins in ins_nt_dict.keys():
					key_root = re.sub(r'(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', key_ins)
					ins_num = re.search(r'_\d+\Z', key_ins).group()[1:]
					if key_root == key:
						gff.write('{}\tblast\tintron\t{}\t{}\t1\t-\t0\tID=ins{}\n'.format(key, ins_nt_dict[key_ins][1], 
							ins_nt_dict[key_ins][2], ins_num))
			else:
				orf_line = '{}\tblast\tCDS\t{}\t{}\t1\t+\t0\tID={}\n'.format(key, orf_nt_dict[key][1], 
					orf_nt_dict[key][2], orf_nt_dict[key][4])
				for key_ins in ins_nt_dict.keys():
					key_root = re.sub(r'(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', key_ins)
					ins_num = re.search(r'_\d+\Z', key_ins).group()[1:]
					if key_root == key:
						gff.write('{}\tblast\tintron\t{}\t{}\t1\t+\t0\tID=ins{}\n'.format(key, ins_nt_dict[key_ins][1], 
							ins_nt_dict[key_ins][2], ins_num))
		gff.write(orf_line)

p57_nt.close()
p57_aa.close()
triat_aa.close()
bexlh_aa.close()
jac_aa.close()
gff.close()
errors.close()