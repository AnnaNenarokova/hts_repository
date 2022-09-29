#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def replace_species_delimeter(infasta, outfasta, old_delimeter="_", new_delimeter="-"):
	out_records = []
	for record in SeqIO.parse(infasta, "fasta"):
		old_id_split = record.id.split(old_delimeter)
		new_id = new_delimeter.join(old_id_split)
		record.id = new_id
		out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def replace_species_delimeter_dir(indir, outdir):
	for fasta in listdir_nohidden(indir):
		infasta = indir + fasta
		outfasta = outdir + fasta
		print (fasta)
		replace_species_delimeter(infasta, outfasta)
	return 0

indir="/Users/anna/work/euk_local/eukprot/font/"
outdir="/Users/anna/work/euk_local/eukprot/font_renamed/"
replace_species_delimeter_dir(indir, outdir)