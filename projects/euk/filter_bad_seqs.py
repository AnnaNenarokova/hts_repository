#!/usr/bin/python3
import os
from Bio import SeqIO
import statistics

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def filter_bad_seqs(infasta, outfasta, len_threshold=0.5):
	all_records = []
	prot_lengths = []
	for record in SeqIO.parse(infasta, "fasta"):
		all_records.append(record)
		prot_lengths.append(len(record.seq))
	prot_median = statistics.median(prot_lengths)

	out_records = []
	for record in all_records:
		seq = record.seq
		bad_symbols = ["X", "U", "*"]
		if (seq[0] == "M") and not(any(x in bad_symbols for x in seq)) and (len(seq)/prot_median > len_threshold):
			out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	
	return 0

infasta="/Users/anna/work/euk_local/cogs_arcogs/COGs/fasta_unfiltered/COG0008.fa"
outfasta="/Users/anna/work/euk_local/cogs_arcogs/COGs/fasta_unfiltered/COG0008_filtered.fa"

def filter_fastas(indir, outdir):
	for fasta in listdir_nohidden(indir):
		infasta = indir + fasta
		outfasta = outdir + fasta
		filter_bad_seqs(infasta, outfasta, len_threshold=0.7)

indir="/Users/anna/work/euk_local/cogs_arcogs/COGs/fasta_unfiltered/"
outdir="/Users/anna/work/euk_local/cogs_arcogs/COGs/fasta_filtered/"
filter_fastas(indir, outdir)