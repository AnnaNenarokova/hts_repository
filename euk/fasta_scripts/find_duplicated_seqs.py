#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def find_duplicated_seqs(fasta_folder):
	seq_dict = {}
	for fasta in listdir_nohidden(fasta_folder):
		fasta_path = fasta_folder + fasta
		for record in SeqIO.parse(fasta_path, "fasta"):
			seqid = record.id
			if seqid not in seq_dict.keys():
				seq_dict[seqid] = fasta
			else:
				print ("duplicated seqid", seqid, fasta, seq_dict[seqid])
	return 0

fasta_folder="/Users/anna/work/euk_local/nina_markers/singlehit_results/archaea/ae_all_filtered/faa/"

find_duplicated_seqs(fasta_folder)