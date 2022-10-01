#!/usr/bin/python3
import os
from Bio import SeqIO

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def read_prot_annotations(fasta_path):
	protid_dict = {}
	i = 0
	for record in SeqIO.parse(fasta_path, "fasta"):
		protid_dict[record.id] = record.description
		if i == 0:
			print(record.description)
		i += 1
	return protid_dict

def get_prot_annotations(fasta_dir):
	protid_dict = {}
	for fasta_file in listdir_nohidden(fasta_dir):
		# print (fasta_file)
		fasta_path = fasta_dir + fasta_file
		protid_dict.update(read_prot_annotations(fasta_path))
	return protid_dict

fasta_dir = "/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset/"
protid_dict = get_prot_annotations(fasta_dir)