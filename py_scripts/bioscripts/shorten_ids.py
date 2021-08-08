#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def shorten_ids(infasta_path, outfasta_path):
    results = []
    for record in SeqIO.parse(infasta, "fasta"):
        old_id = record.id
        new_id = old_id.split("|")[0]
        record.id = new_id
        results.append(record)
    SeqIO.write(results, outfasta, "fasta")
    return 0

folder = 
infasta = folder + "pr2_version_4.13.0_18S_taxo_long.fasta"
outfasta = folder + ""