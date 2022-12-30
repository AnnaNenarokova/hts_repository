#!/usr/bin/python3
from Bio import SeqIO

def get_msa_len_dict(fasta_path):
	msa_len_dict = {}
	for record in SeqIO.parse(fasta_path, "fasta"):
		alignment_no_gaps = record.seq.replace("-","")
		alignment_len = len(alignment_no_gaps)
		msa_len_dict[record.id] = alignment_len

	max_length = max(msa_len_dict.values())
	msa_percent_dict = {}
	for seqid, al_len in msa_len_dict.items():
		msa_percent = 100*al_len/float(max_length)
		msa_percent = '{:.2f}%'.format(msa_percent)
		msa_percent_dict[seqid] = msa_percent
	return msa_percent_dict

fasta_path = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/only_euks/euks_split_markers/only_euks_132_markers_concat.fasta"
msa_len_dict = get_msa_len_dict(fasta_path)