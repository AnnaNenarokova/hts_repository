#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/c_deaminase/PASTA/')
files = os.listdir()

for file in files:
	if '.fa' in file:
		job_desc = file.split('.fa')[0]
		d = 'protein'
		print(file)
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))