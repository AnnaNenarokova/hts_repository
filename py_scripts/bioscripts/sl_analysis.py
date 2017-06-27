#!/usr/bin/python
from Bio import SeqIO
from Bio import pairwise2

# fasta = '/home/anna/bioinformatics/blasto/p57_Trinity_denovo.fasta'
fasta = '/home/anna/bioinformatics/blasto/p57_trinity/de_novo/jaccard_trinity.fasta'
results = []
sl="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG"
sl_len = len(sl)
n_with_sl=0
results = []

for record in SeqIO.parse(fasta, "fasta"):
    forward_seq = record.seq
    reverse_seq = record.reverse_complement().seq
    without_sl = True
    for seq in (forward_seq, reverse_seq):
        exit = False
        for i in range(sl_len-5):
            x = seq.find(sl[i:])
            if (x != -1): #and (x <= i):
                n_with_sl+=1
                exit = True
                break
        if exit == True: break

print n_with_sl
