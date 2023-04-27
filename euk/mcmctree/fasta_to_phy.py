#!/usr/bin/python3
from Bio import AlignIO
from Bio import SeqIO

def fasta_to_phy(infasta, out_phy_path):
	# read the input FASTA file
	alignment = AlignIO.read(infasta, "fasta")

	# write the output in PHYLIP format
	with open(out_phy_path, "w") as outfile:
   		AlignIO.write(alignment, outfile, "phylip-sequential")
	return out_phy_path

infasta = "/Users/vl18625/work/euk/benoit_toy_mcmctree/all_data/shorter_names_phy_2cyanos.fasta"
out_phy_path = "/Users/vl18625/work/euk/benoit_toy_mcmctree/all_data/mcmctree_files/short_names_2cyanos_aln.phy"

fasta_to_phy(infasta, out_phy_path)
