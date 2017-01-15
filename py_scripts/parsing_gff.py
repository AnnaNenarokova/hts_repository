#!/usr/bin/python
inFile = open('/home/kika/blastocrithidia/datasets/Leptomonas_pyrrhocoris_with_UTRs_all_genes_stops_corrected.gff', 'r')

for row in inFile:
	split_row = row.split('\t')
	name = split_row[0]
	attribute = split_row[1]
	feature = split_row[2]
	start = split_row[3]
	stop = split_row[4]
	whatever = split_row[5]
	strand = split_row[6]
	codon = split_row[7]
	description = split_row[8]

	if feature == 'CDS':
		if strand == '+':
			stop = int(stop) + 3
		elif strand == '-':
			if int(start) <= 3:
				start = 1
			else:
				start = int(start) - 3
		else:
			print("error strand")
		new_row = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(name,attribute,feature,start,stop,whatever,strand,codon,description)
	else:
		new_row = row
		
	with open('/home/kika/blastocrithidia/datasets/Lpyr_cds_with_stops.gff', 'a') as result:
		result.write(new_row)