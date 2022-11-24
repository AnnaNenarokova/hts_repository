#!/usr/bin/python3
import os
from Bio import SeqIO
import re
import sys
sys.path.insert(0, "/Users/anna/work/code/ngs/")
sys.path.insert(0, "/user/home/vl18625/code/ngs")
sys.path.insert(0, "/Users/vl18625/work/code/ngs/")
from py_scripts.helpers.parse_csv import *
def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def count_markers(indir, protid_delimiter="-"):
	marker_dict = {}
	marker_set = set()
	for fasta in listdir_nohidden(indir):
		marker_id = fasta.split(".")[0]
		marker_set.add(marker_id)
		fasta_path = indir + fasta
		for record in SeqIO.parse(fasta_path, "fasta"):
			species_id = record.id.split(protid_delimiter)[0]
			if species_id not in marker_dict:
				marker_dict[species_id] = {}
			marker_dict[species_id][marker_id] = "1"
	for species_id in marker_dict:
		for marker_id in marker_set:
			if marker_id not in marker_dict[species_id].keys():
				marker_dict[species_id][marker_id] = 0
	return marker_dict

def add_lineages(marker_dict, tax_info_path, abce=False):
	euk_regex = "\w+_EP\d+"
	tax_info_dict = csv_to_dict(tax_info_path, main_key="gid", delimiter='\t')
	for species_id in marker_dict:
		if re.match(euk_regex, species_id) and abce:
			genome_id = species_id.split("_")[1]
		else:
			genome_id = species_id
		taxonomy =  tax_info_dict[genome_id]["taxonomy"]
		marker_dict[species_id]["taxonomy"] = taxonomy
	return marker_dict

def write_marker_counts(indir, tax_info_path, outpath, protid_delimiter="-",abce=False):
	marker_dict = count_markers(indir, protid_delimiter=protid_delimiter)
	marker_dict = add_lineages(marker_dict, tax_info_path, abce=abce)
	write_dict_of_dicts(marker_dict, outpath, key_name="species_id")
	return outpath

indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/final/linsi_bmge/"
tax_info_path="/Users/vl18625/work/euk/protein_sets/taxa_annotations.tsv"
outpath = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/final/markers_summary.csv"

write_marker_counts(indir, tax_info_path, outpath, protid_delimiter="-",abce=True)