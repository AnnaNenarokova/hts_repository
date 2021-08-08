#!/usr/bin/python
from Bio import SeqIO

def add_number_seqs(infasta, outfasta):
    results = []
    i = 0
    for record in SeqIO.parse(infasta, "fasta"):
        i+=1
        seq_name = record.id
        new_seq_name = str(i) + "_" + seq_name
        record.id = new_seq_name
        results.append(record)
    SeqIO.write(results, outfasta, "fasta")
    return 0

infasta = ""
outfasta = ""

add_number_seqs(infasta, outfasta)