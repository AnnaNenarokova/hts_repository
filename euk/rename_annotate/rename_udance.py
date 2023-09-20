#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def rename_fasta(infasta_path, outfasta_path, delimiter="_"):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		old_id = record.id
		new_id = old_id.split(delimiter)[0]
		record.id = new_id
		record.description = ""
		out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def rename_fastas(indir, outdir):
	for fasta_file in listdir_nohidden(indir):
		infasta_path = indir + fasta_file
		outfasta_path = outdir + fasta_file
		rename_fasta(infasta_path, outfasta_path)
	return outdir

indir="/Users/vl18625/work/haicai/input_alignments/"
outdir="/Users/vl18625/work/haicai/alignments/"
rename_fastas(indir, outdir)