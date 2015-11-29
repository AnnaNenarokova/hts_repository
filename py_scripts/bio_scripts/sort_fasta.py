#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
f = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/SS_39_CRISPR/first_10_kb_t5/t5/pT7blue-G8esc_rev/KD263_CRISPR_region/pt7blue-T4/T4_genome/BW25113/BL21/pBad/unaligned.fasta'
f_out = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/unique_spacers.fasta'
unique_spacers = set()
# for dic in lis:
#    for val in dic.values():
#       s.add(val)
for record in SeqIO.parse(f, "fasta"):
	unique_spacers.add(str(record.seq))

out = []
for record in unique_spacers:
	out.append(SeqRecord(Seq(record, generic_dna)))

SeqIO.write(out, f_out, "fasta")