#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/nucleoporins/jac_new_assembly/PASTA/')
files = os.listdir()

for file in files:
	if '.fa' in file:
		job_desc = file.split('.f')[0]
		d = 'protein'
		print(file)
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))