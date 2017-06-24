#!/usr/bin/python3

def get_stops_gff(gff_path):
	stop_positions = {}
	with open(gff_path, 'r') as gff_file:
		for row in gff_file:
			split_row = row.split('\t')
			name = split_row[0]
			attribute = split_row[1]
			feature = split_row[2]
			start = split_row[3]
			stop = split_row[4]
			score = split_row[5]
			strand = split_row[6]
			codon = split_row[7]
			description = split_row[8]
	gff_file.close()
	return (stop_positions)
