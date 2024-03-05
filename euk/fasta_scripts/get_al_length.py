#!/usr/bin/python3
from Bio import SeqIO
import sys
sys.path.insert(0, "/Users/anna/work/code/ngs/")
sys.path.insert(0, "/user/home/vl18625/code/ngs")
sys.path.insert(0, "/Users/vl18625/work/code/ngs/")
from py_scripts.helpers.parse_csv import *

def get_msa_len_dict(fasta_path):
	msa_len_dict = {}
	for record in SeqIO.parse(fasta_path, "fasta"):
		alignment_no_gaps = str(record.seq).replace("-","")
		alignment_len = len(alignment_no_gaps)
		msa_len_dict[record.id] = alignment_len

	max_length = max(msa_len_dict.values())
	msa_percent_dict = {}
	for seqid, al_len in msa_len_dict.items():
		msa_percent = 100*al_len/float(max_length)
		msa_percent = '{:.2f}'.format(msa_percent)
		msa_percent_dict[seqid] = msa_percent
	return msa_percent_dict

fasta_path="/Users/vl18625/work/euk/molecular_clock/22_02_24/abce_94_markers_concat.fasta"
outpath="/Users/vl18625/work/euk/molecular_clock/22_02_24/abce_94_markers_msa_len.csv"
msa_len_dict = get_msa_len_dict(fasta_path)

write_dict(msa_len_dict, outpath, delimiter=",")