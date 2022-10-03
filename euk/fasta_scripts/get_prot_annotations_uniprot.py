#!/usr/bin/python3
import os
from Bio import SeqIO

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def shorten_annotation(description, protid_delimiter="-"):
	split_description = description.split(" ")
	prot_id = split_description[0]
	prot_id = prot_id.replace("_",protid_delimiter)
	id = split_description[2]
	split_id = id.split("_")
	species = " ".join(split_id[1:-1])

	gene_product_re = "gene_product="
	if "product=" in description:
		if gene_product_re in description:
			split_annotation = description.split(" | ")
			for annot_element in split_annotation:
				if gene_product_re in annot_element:
					function = annot_element.split(gene_product_re)[1]
		else:
			function = description.split("product=")[1].split('protein_id=')[0]
			function = function.strip('"')
	elif "description:" in description:
		function = description.split("description:")[1]
	elif any(gene_re in description for gene_re in ("TRINITY", "|", "ORF type:", "gene_biotype:")):
		function = "predicted gene"
	else:
		function = " ".join(split_description[2:])
	short_annotation = " ".join([species, prot_id, function])
	return short_annotation

def read_prot_annotations(fasta_path):
	protid_dict = {}
	i = 0
	for record in SeqIO.parse(fasta_path, "fasta"):
		description = record.description
		short_annotation = shorten_annotation(description)
		protid_dict[record.id] = short_annotation
	return protid_dict

def get_prot_annotations(fasta_dir):
	protid_dict = {}
	for fasta_file in listdir_nohidden(fasta_dir):
		print (fasta_file)
		fasta_path = fasta_dir + fasta_file
		protid_dict.update(read_prot_annotations(fasta_path))
	return protid_dict

fasta_dir = "/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset/"
protid_dict = get_prot_annotations(fasta_dir)