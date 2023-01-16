#!/usr/bin/python3
from Bio import SeqIO

def make_dayhoff_dict(option):
	dayhoff_4 = {
		"A" : ("A","G","N","P","S","T"),
		"C" : ("C","H","W","Y"),
		"G" : ("D","E","K","Q","R"),
		"T" : ("F","I","L","M","V"),
		"-" : ("-", "X")
		}
	if option == "dayhoff_4":
		dayhoff_dict = dayhoff_4
	recording_dict = {}
	for key in dayhoff_dict:
		for aa in dayhoff_dict[key]:
			recording_dict[aa] = key
	return recording_dict

def recode_seq(in_seq, recording_dict):
	out_seq = ""
	for in_char in in_seq:
		if in_char in recording_dict:
			out_char = recording_dict[in_char]
		else:
			out_char = "-"
			print (in_char, "not in the dict!")
		out_seq += out_char
	return out_seq

def recode_alignment(infile, outfile, option="dayhoff_4"):
	recording_dict = make_dayhoff_dict(option=option)
	out_records = []
	for record in SeqIO.parse(infile, "fasta"):
		recoded_seq = recode_seq(record.seq, recording_dict)
		record.seq = Seq(recoded_seq)
		out_records.append(record)
	SeqIO.write(out_records, outfile, "fasta")
	return outfile

infile = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/final/abce_94_markers_filtered_16_01.fasta"
outfile = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/final/abce_94_markers_16_01_dayhoff4_recoded.fasta"
recode_alignment(infile, outfile, option="dayhoff_4")