#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

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

def parse_seqid_files(seqid_folder):
	seqid_dict = {}
	seqids_set = set()
	for seqid_file in listdir_nohidden(seqid_folder):
		name = seqid_file.split(".")[0]
		seqid_list_path = seqid_folder + seqid_file
		seqid_list = read_list(seqid_list_path)
		seqid_dict[name] = seqid_list
		seqids_set.update(seqid_list)
	return seqid_dict, seqids_set

def prepare_seq_dict(fasta_folder, seqids_set):
	seq_dict = {}
	for fasta in listdir_nohidden(fasta_folder):
		print (fasta)
		fasta_path = fasta_folder + fasta
		for record in SeqIO.parse(fasta_path, "fasta"):
			seqid = record.id
			if seqid in seqids_set:
				seq_dict[seqid] = record
	return seq_dict

def prepare_fastas(seqid_folder, fasta_folder, out_folder):
	print ("Parcing seqid files")
	seqid_dict, seqids_set = parse_seqid_files(seqid_folder)
	print ("Parcing fastas")
	seq_dict = prepare_seq_dict(fasta_folder, seqids_set)
	print ("Writing results")
	for name in seqid_dict:
		outpath = out_folder + name + ".faa"
		out_records = []
		for seqid in seqid_dict[name]:
			record = seq_dict[seqid]
			out_records.append(record)
		SeqIO.write(out_records, outpath, "fasta")
	return out_folder

seqid_folder = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/26_markers/abc_dataset/abc_euks_ids/"
fasta_folder = "/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset/"
out_folder = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/26_markers/abc_dataset/abc_euks_fasta/"

prepare_fastas(seqid_folder, fasta_folder, out_folder)