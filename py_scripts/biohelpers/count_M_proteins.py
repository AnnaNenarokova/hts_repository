#!/usr/bin/python
from Bio import SeqIO
def count_right_prot(fasta_path):
	m_starts = 0
	other_starts = 0
	for record in SeqIO.parse(fasta_path, "fasta"):
		if record.seq[0] == 'M': m_starts += 1
		else: other_starts += 1
	return m_starts, other_starts