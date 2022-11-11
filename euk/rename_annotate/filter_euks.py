#!/usr/bin/python3
from Bio import SeqIO
import re
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def filter_euks_fasta(infasta, outfasta, abce=False):
	out_records = []
	if abce:
		euk_regex = "^\w+_EP\d+-P\d+"
	else:
		euk_regex = "^EP\d+_P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		if re.match(euk_regex, record.id):
			out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_euks_dir(indir, outdir, abce=False):
	for fasta in listdir_nohidden(indir):
		infasta = indir + fasta
		outfasta = outdir + fasta
		filter_euks_fasta(infasta, outfasta, abce=abce)
	return outdir

indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/abc_dataset/final_abce_fastas/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/abc_dataset/final_abce_only_euks_fastas/"

filter_euks_dir(indir, outdir,abce=True)