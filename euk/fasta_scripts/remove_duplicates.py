#!/usr/bin/python3
from os import listdir
from Bio import SeqIO

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def remove_duplicates_fasta(fasta_in, fasta_out):
	out_records = []
	set_ids = set()
	for record in SeqIO.parse(fasta_in, "fasta"):
		if record.id not in set_ids:
			out_records.append(record)
		set_ids.add(record.id)
	SeqIO.write(out_records, fasta_out, "fasta")
	return 0

def remove_duplicates(indir, outdir):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		fasta_in = indir + fasta
		fasta_out = outdir + fasta
		remove_duplicates_fasta(fasta_in, fasta_out)
	return 0

indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/abc_dataset/abce_set_duplicated/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/abc_dataset/abce_set_dedup/"
remove_duplicates(indir, outdir)