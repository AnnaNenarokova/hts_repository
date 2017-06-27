#!/usr/bin/python3
import os
import re
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/')
files = os.listdir()

for file in files:
	if ('sra' not in file and '_fw.fq' in file) or ('sra' not in file and '_rev.fq' in file):
		print(file)
		file_name = file.split('.')[0]
		out = open('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/' + file_name + '_upd.fq', 'w')

		for read in SeqIO.parse(file, 'fastq'):
			print(read.description)
			read.description = re.sub(r'(?P<name>SRR\d+.\d+).(?P<num>\d) \d+ (?P<length>.*)', '\g<2> \g<3>', read.description)
			out.write(read.format('fastq'))