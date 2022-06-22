#!/usr/bin/python3
import os
from Bio import SeqIO

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

indir="/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset_old/"
outdir="/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset/"
replace_species_delimeter_dir(indir, outdir)