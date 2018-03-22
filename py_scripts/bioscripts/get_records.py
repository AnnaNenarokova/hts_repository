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
        f.closed
    for record in SeqIO.parse(fasta_file, "fasta"):
        id = record.id
        if id in keep_list:
            results.append(record)
            not_found_list.remove(id)
    print ('Not found:', not_found_list)
    SeqIO.write(results, outpath, "fasta")
    return 0

fasta_file = 'D:/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome_paper/E_gracilis_transcriptome_final.PROTEINS.fasta'
list_file = 'D:/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome_paper/mitoproteome_datasets/egracilis_all_mito_fraction_list.csv'
outpath = 'D:/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome_paper/mitoproteome_datasets/egracilis_all_mito_fraction_list.faa'

keep_from_list(fasta_file, list_file, outpath)