#!/usr/bin/python3
from Bio import SeqIO

def cut_seqs(infasta,outfasta,upto=100):
	outrecords = []
	for record in SeqIO.parse(infasta, "fasta"):
		if len(record.seq) > upto:
			outrecords.append(record[0:upto])
	SeqIO.write(outrecords, outfasta, "fasta")
	return outfasta


infasta = "/Users/vl18625/work/blasto_local/3_UTR/extracted_3UTRs.fasta"
outfasta = "/Users/vl18625/work/blasto_local/3_UTR/extracted_3UTRs_first_30nt.fasta"

cut_seqs(infasta,outfasta,upto=100)