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

def keep_from_list(fasta_file, keep_list, outpath):
    results=[]
    not_found_list = keep_list
    i = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        if i % 100000 == 0: print (i)
        i+=1
        id = record.id
        if id in keep_list:
            results.append(record)
            not_found_list.remove(id)
    print ('Not found:', not_found_list)
    SeqIO.write(results, outpath, "fasta")
    return 0

def keep_from_listfile(fasta_file, list_file, outpath):
    keep_list=[]
    with open(list_file) as f:
        for line in f:
            keep_list.append(line.rstrip())
    keep_from_list(fasta_file, keep_list, outpath)
    return 0

def exclude_fasta(fasta_in, fasta_exclude, outpath):
    exclude_list = []
    results = []
    i = 0
    for record in SeqIO.parse(fasta_exclude, "fasta"):
        if i % 10000 == 0: print (i)
        i+=1
        id = record.id
        exclude_list.append(id)

    i = 0
    for record in SeqIO.parse(fasta_in, "fasta"):
        if i % 10000 == 0: print (i)
        i+=1
        id = record.id
        if id not in exclude_list:
            results.append(record)
    SeqIO.write(results, outpath, "fasta")
    return 0
