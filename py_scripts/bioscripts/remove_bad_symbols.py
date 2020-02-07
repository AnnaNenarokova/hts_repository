#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
fasta_file = "/home/anna/bioinformatics/diplonema/dataset/no_dpapi_refdataset.faa"
out = "/home/anna/bioinformatics/diplonema/dataset/no_dpapi_refdataset_cleaned"

results = []
i=0
a=1
for record in SeqIO.parse(fasta_file, "fasta"):
    i+=1
    if i%100000 == 0: print i
    old_seq = record.seq
    if '-' in old_seq:
        record.seq = Seq(str(old_seq).replace("-", "X"),old_seq.alphabet)
    results.append(record)
    if i%1000000 == 0:
        outfile = out + str(a) + ".faa"
        SeqIO.write(results, outfile, "fasta")
        a+=1
        results=[]

outfile = out + str(a) + ".faa"
SeqIO.write(results, outfile, "fasta")
