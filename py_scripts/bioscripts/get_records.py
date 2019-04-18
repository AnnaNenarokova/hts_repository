#!/usr/bin/python
from Bio import SeqIO

def keep_n_first(fasta_file, outhpath, n):
    results = []
    i = 0
    for record in SeqIO.parse(fasta, "fasta"):
        if i < n:
            results.append(record)
            i+=1
    SeqIO.write(results, outpath, "fasta")
    return 0

def keep_from_list(fasta_file, list_file, outpath):
    keep_list=[]
    results=[]
    not_found_list = keep_list
    with open(list_file) as f:
        for line in f:
            keep_list.append(line.rstrip())
    for record in SeqIO.parse(fasta_file, "fasta"):
        id = record.id
        if id in keep_list:
            results.append(record)
            not_found_list.remove(id)
    print ('Not found:', not_found_list)
    SeqIO.write(results, outpath, "fasta")
    return 0

fasta_file = '/home/vl18625/bioinformatics/diplonema/Dp_PB-MI_190104_dedup_cut_l100.faa'
list_file = '/home/vl18625/bioinformatics/diplonema/hgt_cases.csv'
outpath = '/home/vl18625/bioinformatics/diplonema/hgt_cases.faa'

keep_from_list(fasta_file, list_file, outpath)