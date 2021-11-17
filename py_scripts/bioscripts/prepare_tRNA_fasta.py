#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

def add_aragorn_record(record, tRNA_dict, species):
	tRNA_aragorn = record.description.split(" ")[1]
	if tRNA_aragorn != "tmRNA":
		tRNA_split = tRNA_aragorn.split("-")[1].split("(")
		amino_acid = tRNA_split[0]
		codon = tRNA_split[1].rstrip(")")
		tRNA_type = amino_acid + "_" + codon
		tRNA_name = tRNA_type + "_" + species
		if tRNA_type not in tRNA_dict.keys():
			tRNA_dict[tRNA_type] = {}
		if tRNA_name in tRNA_dict[tRNA_type]:
			i = 2
			new_tRNA_name = tRNA_name + "_" + str(i)
			while new_tRNA_name in tRNA_dict[tRNA_type]:
				i += 1
				new_tRNA_name = tRNA_name + "_" + str(i)
			tRNA_name = new_tRNA_name
		new_record = record
		new_record.id = tRNA_name
		tRNA_dict[tRNA_type][tRNA_name] = new_record
	return tRNA_dict

def prepare_tRNA_dict(aragorn_fasta_folder):
	tRNA_dict = {}
	for filename in listdir(aragorn_fasta_folder):
		if filename[0] != ".":
			fasta_file = aragorn_fasta_folder + filename
			species = filename.split(".")[0]
			for record in SeqIO.parse(fasta_file, "fasta"):
				tRNA_dict = add_aragorn_record(record, tRNA_dict, species)
	return tRNA_dict

def write_tRNA_fastas(tRNA_dict, outfolder):
	for tRNA_type in tRNA_dict:
		if "?" not in tRNA_type:
			result = []
			outfile_path= outfolder + tRNA_type + ".fasta"
			for tRNA in tRNA_dict[tRNA_type]:
				tRNA_record = tRNA_dict[tRNA_type][tRNA]
				result.append(tRNA_record)
			SeqIO.write(result, outfile_path, "fasta")
	return 0

aragorn_fasta_folder = "/Users/anna/work/blasto_local/tRNA/fasta_test/"
outfolder = "/Users/anna/work/blasto_local/tRNA/test/"
tRNA_dict = prepare_tRNA_dict(aragorn_fasta_folder)
write_tRNA_fastas(tRNA_dict, outfolder)