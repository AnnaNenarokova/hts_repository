#!/usr/bin/python
import csv
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
global ONLY_ONE_HIT; ONLY_ONE_HIT = False

handle_file = '/home/anna/bioinformatics/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = open(handle_file)
handle_csv = csv.reader(handle_file, delimiter=',')

if ONLY_ONE_HIT:
	sorted_csv = sorted( handle_csv, key = lambda x: ( x[0], -int(x[3]), -float(x[2]) ) ) 

	results = []
	cur_seq = None
	for row in sorted_csv:
		if row[0] != cur_seq: 
			cur_seq = row[0]
			results.append(row)
	handle_file.close()
else: 
	results = []
	for row in handle_csv:
		results.append(row)

fasta_file = '/home/anna/bioinformatics/wheat/wheat_scaffolds.fasta'
result_seqs = []
for seq_record in SeqIO.parse(fasta_file, "fasta"):
	for row in results:
		if seq_record.id == row[1]:
			start = int(row[8])
			end = int(row[9])
			if start > end: start, end = end, start
			seq = seq_record.seq[start:end]
			result_seqs.append(SeqRecord(seq=seq, id=seq_record.id + ' ' + row[0], description=''))
			if ONLY_ONE_HIT: results.remove(row)

out_file = '/home/anna/bioinformatics/wheat/nbs_lrr_new_assembly.fasta'	
SeqIO.write(result_seqs, out_file, "fasta")
