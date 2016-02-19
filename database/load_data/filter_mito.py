#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *
from py_scripts.common_helpers.flatten import *
from Bio import SeqIO

def filter_mito(mitolist_path, fasta_path, outpath):
    mitolist = flatten(parse_csv(mitolist_path))
    results = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        if record.id in mitolist:
            results.append(record)
    SeqIO.write(results, outpath, "fasta")
    return outpath

mitolist_path = '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/mitolist.csv'
fasta_path = '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_orf_trans_all.fasta'
outpath =  '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.fasta'

filter_mito(mitolist_path, fasta_path, outpath)