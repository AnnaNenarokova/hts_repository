#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def split_euk_fasta(marker_name, fasta_path, outdir):
	seq_dict = {}
	print (marker_name)
	for record in SeqIO.parse(fasta_path, "fasta"):
		split_record = record.id.split("_")
		source = split_record[0]
		seqid = split_record[1]
		if source not in seq_dict.keys():
			seq_dict[source] = []
		record.id = seqid
		seq_dict[source].append(record)
	for source in seq_dict:
		outpath = outdir + marker_name + "_" + source + ".faa"
		SeqIO.write(seq_dict[source], outpath, "fasta")
	return 0

def split_euk_fastas(indir, outdir):
	for marker_file in listdir_nohidden(indir):
		marker_name = marker_file.split(".")[0]
		fasta_path = indir + marker_file
		split_euk_fasta(marker_name, fasta_path, outdir)
	return 0 

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/abe/only_euks/final_abce_only_euks_fastas/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/abe/only_euks/euks_split_markers/faa/"

split_euk_fastas(indir, outdir)