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

seqid_folder = "/Users/anna/work/euk_local/nina_markers/ABE/5_markers/euk_ids/euk_alpha/"
fasta_folder = "/Users/anna/work/euk_local/eukprot/anna_eukprot_first_renamed/"
out_folder = "/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/faa_euk_alpha/"
prepare_fastas(seqid_folder, fasta_folder, out_folder)

seqid_folder = "/Users/anna/work/euk_local/nina_markers/ABE/5_markers/euk_ids/euk_cyano/"
fasta_folder = "/Users/anna/work/euk_local/eukprot/anna_eukprot_first_renamed/"
out_folder = "/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/faa_euk_cyano/"
prepare_fastas(seqid_folder, fasta_folder, out_folder)