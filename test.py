import csv
f = open('/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/fuzznuc_report')
csv_f = csv.reader(f, delimiter='\t')

for row in csv_f:
	print row

f.close()
