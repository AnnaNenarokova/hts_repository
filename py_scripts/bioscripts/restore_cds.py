#!/usr/bin/python
from py_scripts.helpers.parse_csv import *
from Bio import SeqIO
from Bio import Seq

transcriptome_path=[]
blast_csv_path=[]
def restore_cds(blast_csv_path, transcriptome_path)
    blast_hits = parse_csv(blast_csv_path)
    results = []
    for bh in blast_hits:

