#!/usr/bin/python3
import os

os.chdir('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/')
files = os.listdir()

for file in files:
	if ('sra' in file and '_fw.fq' in file) or ('sra' in file and '_rev.fq' in file):
		print(file)
		file_name = file.split('.')[0]
		out = open('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/' + file_name + '_upd.fq', 'w')
		infile = open(file).read()
		lines = infile.split('\n')
		for line in lines:
			if line.startswith('@SRR'):
				#@SRR2173361.101.1 HWI-ST885:166:H84KHADXX:1:1101:2021:2092 length=100
				#@SRR2173361.101.2 HWI-ST885:166:H84KHADXX:1:1101:2021:2092 length=100
				print(line)
				description = (line.split(' ')[0].split('.')[0] + '.' + line.split(' ')[0].split('.')[1] + ' ' + 
					line.split(' ')[0].split('.')[2] + ' ' + line.split(' ')[1])
				out.write(description + '\n')
			else:
				out.write(line + '\n')

	if ('sra' not in file and '_fw.fq' in file) or ('sra' not in file and '_rev.fq' in file):
		print(file)
		file_name = file.split('.')[0]
		out = open('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/' + file_name + '_upd.fq', 'w')
		infile = open(file).read()
		lines = infile.split('\n')
		for line in lines:
			if line.startswith('@SRR'):
				#@SRR1186295.25.1 25 length=100
				#@SRR1186295.25.2 25 length=100
				print(line)
				description = (line.split(' ')[0].split('.')[0] + '.' + line.split(' ')[0].split('.')[1] + ' ' + 
					line.split(' ')[0].split('.')[2])
				out.write(description + '\n')
			else:
				out.write(line + '\n')