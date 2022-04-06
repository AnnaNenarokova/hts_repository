#!/usr/bin/python3
import os
from Bio import SeqIO

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def check_fastas(indir, outpath):
	bad_symbols = ["X", "U", "*", "-", "+"]
	out_list = []
	with open(outpath, "w") as outfile:
		i = 0
		for fasta_file in listdir_nohidden(indir):
			if i % 10 == 0:
				print (i)
			bad_seq_n = 0
			all_seq_n = 0
			fasta_path = indir + fasta_file
			for record in SeqIO.parse(fasta_path, "fasta"):
				all_seq_n += 1
				if any(x in bad_symbols for x in record.seq[:-1]):
					bad_seq_n += 1
			species_info = fasta_file.split(".fasta")[0]
			species_info_split = species_info.split("_")
			id = species_info_split[0]
			out_list =[id, species_info, str(bad_seq_n), str(all_seq_n)]
			out_line = "\t".join(out_list) + "\n"
			outfile.write(out_line)
			i +=1
	return outpath

# indir = "/Users/vl18625/work/euk/eukprot/eukprot3/proteins/"
# outpath = "/Users/vl18625/work/euk/eukprot/eukprot3/bad_seqs_stats.tsv"

indir = "/user/work/vl18625/euk/eukprot/eukprot2/proteins/"
outpath = "/user/work/vl18625/euk/eukprot/eukprot2/eukprot2_bad_seqs_stats.tsv"

check_fastas(indir, outpath)