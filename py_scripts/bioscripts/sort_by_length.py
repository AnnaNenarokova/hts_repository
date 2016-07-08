#!/usr/bin/python
from Bio import SeqIO

fasta_file = '/home/anna/Dropbox/phd/bioinformatics/genomes/hemistasia/Hemistasia_cutadapt_trinity_run3.fasta'
out_file = '/home/anna/Dropbox/phd/bioinformatics/genomes/hemistasia/Hemistasia_cutadapt_trinity_run3_sorted.fasta'
seqs = list(SeqIO.parse(fasta_file, "fasta"))
print len(seqs[0].seq)
seqs = sorted(seqs, key=lambda seqrecord: -len(seqrecord.seq))
print len(seqs[0].seq)
SeqIO.write(seqs, out_file, "fasta")
