#!/usr/bin/python3
from Bio import SeqIO

def replace_record(infasta, replacing_fasta, id_replace, outfasta):
	replacing_record = SeqIO.read(replacing_fasta, "fasta")
	results = []
	for record in SeqIO.parse(infasta, "fasta"):
		if record.id == id_replace:
			result = replacing_record
		else:
			result = record
		results.append(result)
	SeqIO.write(results, outfasta, "fasta")
	return 0

infasta="/Users/vl18625/work/blasto_local/p57_ra_polished.fa"
replacing_fasta="/Users/vl18625/work/blasto_local/Ctg28_corrected.fasta"
id_replace="Ctg28_length_81690"
outfasta="/Users/vl18625/work/blasto_local/bnonstop_corrected_assembly.fasta"
replace_record(infasta, replacing_fasta, id_replace, outfasta)