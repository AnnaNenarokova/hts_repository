#!/usr/bin/python3
import re
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f


def get_eukprot_seqs(in_fasta, out_fasta):
	euk_regex = "^EP\d+_P\d+"
	out_records = []
	for record in SeqIO.parse(in_fasta, "fasta"):
		seqid = record.id
		if re.match(euk_regex, seqid):
			out_records.append(record)
	SeqIO.write(out_records, out_fasta, "fasta")
	return out_fasta

def get_eukprot_seqs_dir(indir, outdir):
	for fasta_file in listdir_nohidden(indir):
		in_fasta = indir + fasta_file
		out_fasta = outdir + fasta_file
		print(in_fasta)
		get_eukprot_seqs(in_fasta, out_fasta)
	return outdir

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/faa1/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/mono_set_1/euk_fastas_1/"
get_eukprot_seqs_dir(indir, outdir)