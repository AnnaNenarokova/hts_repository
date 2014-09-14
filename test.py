import csv
f = open('/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/fuzznuc_report')
csv_f = csv.reader(f, delimiter='\t')
repeat_matches = []

for row in csv_f:
	if row[0] != 'SeqName':
		repeat_matches.append({ 'SeqName': row[0], 'Start': row[1], 'End': row[2], 'Strand': row[4], 'Mismatch': row[6] })
		# repeat_matches.append([row[0], row[1], row[2], row[4], row[6]])

# print repeat_matches 

f.close()
