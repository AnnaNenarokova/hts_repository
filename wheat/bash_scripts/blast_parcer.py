#!/usr/bin/python
import csv
from Bio import SeqIO

handle_file = '/home/anna/bioinformatics/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = open(handle_file)
handle_csv = csv.reader(handle_file, delimiter=',')
sorted_csv = sorted( handle_csv, key = lambda x: ( x[0], -int(x[3]), -float(x[2]) ) ) 

results = []

cur_seq = None
print len(sorted_csv)
for row in sorted_csv:
	if row[0] != cur_seq: 
		cur_seq = row[0]
		results.append(row)

for 