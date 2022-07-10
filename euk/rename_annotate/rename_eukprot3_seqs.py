#!python3
from os import listdir
from Bio import SeqIO

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

def rename_seq(old_name):
	old_name_split = old_name.split("_")
	new_name = old_name_split[0] + "-" + old_name_split[-1]
	return new_name

def rename_seqs(infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		old_name = record.id
		new_name = rename_seq(old_name)
		record.id = new_name
		out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def rename_seqs_dir_keep_list(indir, outdir, keep_list_path=False):
	if keep_list_path:
		keep_list = read_list(keep_list_path)
	for fasta in listdir_nohidden(indir):
		fasta_id = fasta.split("_")[0]
		if not keep_list_path or (fasta_id in keep_list):
			print (fasta)
			infasta_path = indir + fasta
			outfasta_path = outdir + fasta
			rename_seqs(infasta_path, outfasta_path)
	return outdir


keep_list_path = "/Users/anna/work/euk_local/eukprot/new_eukprot3_proteomes_list.txt"
indir = "/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_archaea_faa/"
outdir = "/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_archaea_faa_renamed/"

rename_seqs_dir_keep_list(indir, outdir)