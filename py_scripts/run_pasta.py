#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/pasta/without_anticodon/')
files = os.listdir()

for file in files:
	if '.fasta' in file:
		job_desc = file.split('.f')[0]
		print(file)
		os.system('run_pasta.py -i {} -d dna -j {}'.format(file, job_desc))