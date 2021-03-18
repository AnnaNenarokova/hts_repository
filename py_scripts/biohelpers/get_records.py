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


fasta_in = '/Users/annanenarokova/work/blasto_local/tRNAs/tRNAseq/P57-cyto_trimmed_vsearch_out.fasta'
keep_list = '/Users/annanenarokova/work/blasto_local/tRNAs/tRNAseq/unknown_vsearch_clusters.txt'
outpath = '/Users/annanenarokova/work/blasto_local/tRNAs/tRNAseq/unknown_vsearch_clusters.fasta'


keep_from_list(fasta_in, keep_list, outpath)