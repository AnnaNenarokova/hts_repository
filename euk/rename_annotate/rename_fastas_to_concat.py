#!/usr/bin/python3
from Bio import SeqIO
import re
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def rename_fasta_to_concat(infasta, outfasta):
	# euk_regex = "^EP\d+_P\d+"
	euk_regex = "^EP\d+\S+_P\d"

	out_records = []
	for record in SeqIO.parse(infasta, "fasta"):
		old_id = record.id
		if re.match(euk_regex, old_id):
			delimiter = "_"
		else:
			delimiter = "-"
		new_id = old_id.split(delimiter)[0]
		record.id = new_id
		record.description = ""
		out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return outfasta

def rename_fastas_to_concat(indir, outdir):
	for fasta in listdir_nohidden(indir):
		infasta = indir + fasta
		outfasta = outdir + fasta
		rename_fasta_to_concat(infasta, outfasta)
	return outdir

indir="/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/ce_filtered/linsi_bmge/"
outdir="/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/ce_filtered/linsi_bmge_renamed/"
rename_fastas_to_concat(indir, outdir)