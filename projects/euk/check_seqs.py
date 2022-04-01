#!/usr/bin/python3
import os
from Bio import SeqIO

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def check_fastas(indir):
	bad_symbols = ["X", "U", "*"]
	for fasta_file in listdir_nohidden(indir):
		print(fasta_file)
		fasta_path = indir + fasta_file
		for record in SeqIO.parse(fasta_path, "fasta"):
			if any(x in bad_symbols for x in record.seq):
				print (record.id)
	return 0

indir = "/Users/anna/work/euk_local/nina_markers/BacEuk_markers_faa/"

check_fastas(indir)