#!/usr/bin/python3
from os import listdir
from Bio import SeqIO
from Bio.Seq import Seq
import re

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def read_list(list_path):
	result_list = []
	with open (list_path) as list_file:
		for line in list_file:
			result_list.append(line.rstrip())
	return result_list

def filter_fastas_exclude_sp(exclude_list, indir, outdir, species_id_delimiter="_"):
	for file_name in listdir_nohidden(indir):
		infile = indir + file_name
		out_records = []
		for record in SeqIO.parse(infile, "fasta"):
			species_id = record.id.split(species_id_delimiter)[0]
			if species_id not in exclude_list:
				out_records.append(record)
		outfile = outdir + file_name
		SeqIO.write(out_records, outfile, "fasta")
	return 0

def filter_fastas_exclude_sp_new(exclude_list, indir, outdir):
	for file_name in listdir_nohidden(indir):
		infile = indir + file_name
		out_records = []
		for record in SeqIO.parse(infile, "fasta"):
			species_id = record.id.split("-")[0]
			try:
				species_id = species_id.split("_")[1]
			except:
				pass
			if species_id not in exclude_list:
				out_records.append(record)
		outfile = outdir + file_name
		SeqIO.write(out_records, outfile, "fasta")
	return 0

def filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter="-", euk=False):
	out_records = []
	euk_regex = "^EP\d+-P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		species_id = record.id.split(species_id_delimiter)[0]
		if euk:
			if re.match(euk_regex, record.id):
				if species_id in keep_list:
					out_records.append(record)
			else:
				out_records.append(record)
		else:
			if species_id in keep_list:
				out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_abce_keep_sp(keep_list, infasta, outfasta):
	out_records = []
	# euk_regex = "\w+_EP\d+-P\d+"
	euk_regex = "EP\d+_\S+_P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		seq_id = record.id.split("-")[0]
		if re.match(euk_regex, record.id):
			species_id = seq_id.split("_")[0]
		else:
			species_id = seq_id
		if species_id in keep_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_fastas_keep_sp(keep_list, indir, outdir, species_id_delimiter="-", euk=False, abce=False):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		infasta = indir + fasta
		outfasta = outdir + fasta
		if abce:
			filter_abce_keep_sp(keep_list, infasta, outfasta)
		else:
			filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter=species_id_delimiter,euk=euk)
	return 0 

def filter_fastas_keep_sp_read_list(list_dir, indir, outdir, list_ext=".txt", euk=False):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		name = fasta.split(".")[0]
		infasta = indir + fasta
		outfasta = outdir + fasta
		keep_list_path = list_dir + name + list_ext
		print(keep_list_path)
		try:
			keep_list = read_list(keep_list_path)
		except:
			print(keep_list_path, "not found")
		else:
			filter_fasta_keep_seqs(keep_list, infasta, outfasta, euk=euk)
	return 0 

def filter_fastas_exclude_sp_simple(exclude_list, infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		species_id = record.id
		if species_id not in exclude_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def filter_fasta_keep_seqs(keep_list, infasta_path, outfasta_path, euk=False):
	out_records = []
	euk_regex = "EP\d+_\S+_P\d+"
	for record in SeqIO.parse(infasta_path, "fasta"):
		seq_id = record.id
		if euk:
			if re.match(euk_regex, seq_id):
				if seq_id in keep_list:
					out_records.append(record)
			else:
				out_records.append(record)
		else:
			if seq_id in keep_list:
				out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def remove_euks_fasta(infasta_path, outfasta_path):
	out_records = []
	euk_regex = "\w+_EP\d+-P\d+"
	for record in SeqIO.parse(infasta_path, "fasta"):
		if re.match(euk_regex, record.id):
			pass
		else:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def remove_euks_fastas(indir, outdir):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		infasta_path = indir + fasta
		outfasta_path = outdir + fasta
		remove_euks_fasta(infasta_path, outfasta_path)
	return outdir


keep_list = ["EP00900","EP00279","EP00314","EP01084","EP00390","EP00609","EP01082","EP00820","EP00185","EP00802","EP00466","EP00741","EP00667","EP00931","EP00611","EP00852","EP00210","EP00206","EP00738","EP00202","EP00457","EP00797","EP00271","EP00269","EP00167","EP00248","EP00229","EP00176","GCA_003503675.1","EP00260","EP00895","EP00247","GCA_000155555.1","GCA_003149375.1","GCA_000010065.1","GCA_000484535.1","GCA_001870225.1","GCA_000019485.1","GCA_000015645.1","GCA_000195975.1","GCA_000464785.1","GCA_000018105.1","GCA_000013225.1","GCA_000317065.1","GCA_000353285.1","GCA_002075285.3","GCA_000346485.2","GCA_000204075.1"]
indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/cyano/ce_filtered1_faa/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/cyano/ce_filtered_2_faa/"
filter_fastas_keep_sp(keep_list, indir, outdir, species_id_delimiter="-", euk=True, abce=False)

list_dir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/cyano/euk_mono_cyano/"
indir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/cyano/ce_unfiltered_faa/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/cyano/ce_filtered_faa/"
# filter_fastas_keep_sp_read_list(list_dir, indir, outdir, list_ext=".txt", euk=True)
