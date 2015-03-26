#!/usr/bin/python
from string import find
import csv
from Bio import SeqIO

def read_csv(csv_f):
	csv_data = []
	csv_f = open(csv_f, 'rb')
	reader = csv.reader(csv_f)
	for row in reader: 
		csv_data.append(row)
	csv_f.close()
	return csv_data

def find_barcodes(seq, barcodes):
	min_bc_position = len(seq)
	right_barcode = None
	for barcode in barcodes:
		cur_bc_position = find(seq, barcode[1])
		if (cur_bc_position != -1) and (cur_bc_position < min_bc_position):
			min_bc_position = cur_bc_position
			right_barcode = barcode
			print min_bc_position
	if right_barcode:
		right_barcode.append(min_bc_position)
		print right_barcode
	return right_barcode

barcodes_file = '/home/anna/bioinformatics/wheat/barcodes/right_barcodes.csv'
barcodes = read_csv(barcodes_file)
fastq_file = '/home/anna/bioinformatics/wheat/L_H8_1/trim_out/unpaired_out_rv.fastq'
for seq_record in SeqIO.parse(fastq_file, "fastq"):
	find_barcodes(seq_record.seq, barcodes)
	