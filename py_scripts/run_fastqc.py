#!/usr/bin/python3
import os
import subprocess

os.chdir('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA284294/')
files = os.listdir()

fastqc = '/home/kika/tools/FastQC/fastqc'
out_dir = '/media/4TB1/blastocrithidia/bexlh/reads/fastqc/PRJNA284294/'

for file in files:
	subprocess.call('{} -o {} {}'.format(fastqc, out_dir, file), shell=True)