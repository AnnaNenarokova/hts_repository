#!/usr/bin/python3
import os
import subprocess

os.chdir('/media/4TB1/blastocrithidia/bexlh/reads/raw/PRJNA238835/')
files = os.listdir()

fastqc = '/home/kika/tools/FastQC/fastqc'
out_dir = '/media/4TB1/blastocrithidia/bexlh/reads/fastqc/PRJNA238835/' 

for file in files:
	subprocess.call('{} -o {} {}'.format(fastqc, out_dir, file), shell=True)