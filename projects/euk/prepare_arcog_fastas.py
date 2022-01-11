#!/usr/bin/python3
import re
import os
from Bio import SeqIO

def get_arcog_dict(arcog_info_csv_path, arcog_list_path, delimiter=","):
	arcog_keep_list=[]
	with open(arcog_list_path) as f:
		for line in f:
			arcog_keep_list.append(line.rstrip())

	arcog_dict = {}
	prot_keep_set = set()
	with open(arcog_info_csv_path) as f:
		for line in f:
			line_split = line.rstrip().split(delimiter)
			genome_id = line_split[1]
			prot_id = line_split[2]
			arcog_id = line_split[6]
			if arcog_id in arcog_keep_list:
				if arcog_id not in arcog_dict:
					arcog_dict[arcog_id] = set()
				arcog_dict[arcog_id].add(prot_id)
				prot_keep_set.add(prot_id)				
	return arcog_dict, prot_keep_set

def get_arcog_seq_dict(prot_keep_set, arcog_fasta):
	not_found_list = prot_keep_set
	arcog_seq_dict = {}
	i = 0
	for record in SeqIO.parse(arcog_fasta, "fasta"):
		if i % 100000 == 0: print (i)
		i+=1
		prot_id = record.id
		if prot_id in prot_keep_set:
			not_found_list.remove(prot_id)
			arcog_seq_dict[prot_id] = record
	if len(not_found_list) > 0:
		print ('Not found:', not_found_list)
	return arcog_seq_dict

def write_arcog_fastas(arcog_dict, arcog_seq_dict, outdir):
	for arcog_id in arcog_dict:
		outpath = outdir + arcog_id + ".fa"
		out_records = []
		for prot_id in arcog_dict[arcog_id]:
			seq_record = arcog_seq_dict[prot_id]
			if seq_record.seq[0] == "M":
				out_records.append(arcog_seq_dict[prot_id])
		SeqIO.write(out_records, outpath, "fasta")
	return outdir

def prepare_arcog_fastas(arcog_fasta, arcog_info_csv_path, arcog_list_path, outdir):
	print ("Parcing arCOG info")
	arcog_dict, prot_keep_set = get_arcog_dict(arcog_info_csv_path, arcog_list_path)
	print ("Parcing arCOGdb fasta")
	arcog_seq_dict = get_arcog_seq_dict(prot_keep_set, arcog_fasta)
	print ("Writing down arCOG fastas")
	outdir = write_arcog_fastas(arcog_dict, arcog_seq_dict, outdir)
	return 0
	

arcog_fasta = "/Users/anna/work/euk_local/cogs_arcogs/arCOGs/ar18.fa"
arcog_info_csv_path = "/Users/anna/work/euk_local/cogs_arcogs/arCOGs/ar18.ar14.02.csv"
arcog_list_path = "/Users/anna/work/euk_local/cogs_arcogs/arCOGs/arcogs_selected_nina.txt"
outdir = "/Users/anna/work/euk_local/cogs_arcogs/arCOGs/arcogs_nina_set/fasta/"

prepare_arcog_fastas(arcog_fasta, arcog_info_csv_path, arcog_list_path, outdir)
