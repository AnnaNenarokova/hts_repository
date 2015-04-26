#!/usr/bin/python
import csv
handle_file = '/home/anna/bioinformatics/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = open(handle_file)
handle_csv = csv.reader(handle_file, delimiter=',')
results = []
for row in handle_csv:
	exists = False
	if row[0] != 'query':
		query = row[0]
		for result in results:
			if result[0] == query: 
				exists = True
				break
		if not exists: results.append(row)
	else: results.append(row)

results2 = []
for row in results:
	results2.append('\t'.join(row))

result_file = '/home/anna/bioinformatics/outdirs/alignments/contigs/result_mut9.csv'
result_file = open(result_file, 'w')
result_file.write('\n'.join(results2))
result_file.close