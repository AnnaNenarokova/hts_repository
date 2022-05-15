#!/usr/bin/python
import os
from Bio import SeqIO

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def filter_fastas(exclude_list, indir, outdir):
	for file_name in listdir_nohidden(indir):
		infile = indir + file_name
		out_records = []
		for record in SeqIO.parse(infile, "fasta"):
			species_id = record.id.split("_")[0]
			if species_id not in exclude_list:
				out_records.append(record)
		outfile = outdir + file_name
		SeqIO.write(out_records, outfile, "fasta")
	return 0



exclude_list= ["EP00159", "EP01006"]

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/linsi_bmge/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/linsi_bmge_filtered_species/"

filter_fastas(exclude_list, indir, outdir)