#!/usr/bin/python
from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_path='/home/anna/bioinformatics/all_tryp_references/cds/TriTrypDB-34_TbruceiTREU927_AnnotatedCDSs_filtered.fasta'

codon_usage = False

for record in SeqIO.parse(fasta_path, "fasta"):
    seq_length = len(record.seq)
    if seq_length % 3 != 0:
        print "Error! Len % 3 not equal 0"
    if not codon_usage:
        codon_usage = [{} for x in range(seq_length/3)]
    for i, k in enumerate(range(0, seq_length, 3)):
        codon = str(record.seq[k:k+3])
        if codon in codon_usage[i].keys():
            codon_usage[i][codon]+= 1
        else:
            codon_usage[i][codon] = 1


stop_codons = {
    "TAA"  : [],
    "TAG"  : [],
    "TGA"  : []
}

for pos in codon_usage:
    for stop_codon in stop_codons:
        if stop_codon in pos.keys():
            stop_codons[stop_codon].append(pos[stop_codon])
        else:
            stop_codons[stop_codon].append(0)

# print stop_codons

plots = []

x = range(-400,-1) #+ range (0, 50)
for stop_codon in stop_codons:
    print stop_codon
    coverage = stop_codons[stop_codon]
    print len(coverage)
    new_plot = plt.plot(x,coverage,label=stop_codon)

plt.legend()

plt.show()
