#!/usr/bin/python
from Bio import SeqIO


# fasta = '/home/anna/bioinformatics/blasto/p57_Trinity_denovo.fasta'
fasta = '/home/anna/bioinformatics/blasto/p57_trinity/de_novo/jaccard_trinity.fasta'
results = []
sl="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG"
sl_len = len(sl)
n_without_sl=0
results = []


for record in SeqIO.parse(fasta, "fasta"):
    forward_seq = record.seq
    reverse_seq = record.reverse_complement().seq
    without_sl = True
    for i in range(sl_len-10):
        for seq in (forward_seq, reverse_seq):
            x = seq.find(sl[i:])
            if (x != -1): # and (x <= i):
                without_sl = False
                break
    if without_sl == True: n_without_sl += 1

print n_without_sl
