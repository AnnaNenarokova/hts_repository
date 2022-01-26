#!/usr/bin/python
from Bio import SeqIO

def reverse_seqs(infasta, outfasta):
	results = []
	for record in SeqIO.parse(infasta, "fasta"):
		new_seq = record.seq.reverse_complement()
		record.seq = new_seq
		results.append(record)
	SeqIO.write(results, outfasta, "fasta")
	return 0

infasta="/Users/anna/work/blasto_local/oxopap_ambar/all_clipped/wrong_orientation_all.fasta"
outfasta="/Users/anna/work/blasto_local/oxopap_ambar/all_clipped/wrong_orientation_all_rev.fasta"

reverse_seqs(infasta, outfasta)