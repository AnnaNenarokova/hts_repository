#!/usr/bin/python3
import os
from Bio import SeqIO

def parse_3UTRs(infasta_path, outfasta_path, id_delimiter="-"):
	records_3UTRs = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		id_split = record.id.split(id_delimiter)
		transcript_id = id_split[0]
		polyA_count = int(id_split[1])
		stop_codon = record.seq[:3]
		if stop_codon == "TAA":
			seq_3UTR = record.seq[3:-polyA_count]
			record.name = transcript_id
			record.seq = seq_3UTR
			record.description = ""
			records_3UTRs.append(record)
	SeqIO.write(records_3UTRs, outfasta_path, "fasta")
	return records_3UTRs

def count_codon(seq, codon, frame=0, seq_len=0):
	codon_count = 0
	if seq_len == 0:
		seq_len = len(seq)
	for i in range(frame,seq_len,3):
		triplet = seq[i:i+3]
		if triplet == codon:
			codon_count+=1
	return codon_count

def count_codon_all_frames(records, seq_len=0, codon="TAA"):
	codon_count_frame0 = 0
	codon_count_frame1 = 0
	codon_count_frame2 = 0
	for record in records:
		seq = record.seq
		codon_count_frame0 += count_codon(seq, codon, seq_len=seq_len, frame=0)
		codon_count_frame1 += count_codon(seq, codon, seq_len=seq_len, frame=1)
		codon_count_frame2 += count_codon(seq, codon, seq_len=seq_len, frame=2)
	codon_tuple = (codon_count_frame0, codon_count_frame1, codon_count_frame2)
	return codon_tuple

def prepare_statistics(records):
	codons = ["AAA", "TTT", "TAA", "TAG", "TGA"]
	seq_lens = [3, 6, 9, 12, 15, 0]
	for seq_len in seq_lens:
		for codon in codons:
			codon_tuple = count_codon_all_frames(records, seq_len=seq_len, codon=codon)
			print ("codon", codon, "first", seq_len, "nt of 3'UTRs", codon_tuple)

infasta_path = "/Users/anna/work/blasto_local/tr_UTRs_with_polyas.fasta"
outfasta_path = "/Users/anna/work/blasto_local/extracted_3UTRs.fasta"

records_3UTRs = parse_3UTRs(infasta_path, outfasta_path, id_delimiter="-")

prepare_statistics(records_3UTRs)
