#!/usr/bin/python3
import os

os.chdir('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/thiolation/')
files = os.listdir()

for file in files:
	if '.fasta' in file:
		job_desc = file.split('.f')[0]
		print(file)
		os.system('run_pasta.py -i {} -d protein -j {}'.format(file, job_desc))
