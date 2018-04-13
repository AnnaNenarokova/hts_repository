#!/usr/bin/python3
from Bio import SeqIO
import csv
import re

description_path = "D:/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome/mitoproteome_datasets/mouse_geneid_descriptions.tsv"
fasta_path = "D:/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome/mitoproteome_datasets/fasta/Mouse.MitoCarta2.0.fasta"
outpath = "D:/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome/mitoproteome_datasets/fasta/Mouse.MitoCarta2.0_longest_isoforms.fasta"

with open(description_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
    descriptions_from_csv = {}
    for row in csvreader:
        id = row[0]
        description = row[1]
        descriptions_from_csv[id] = description

isoforms = {}

for record in SeqIO.parse(fasta_path, "fasta"):
    description = record.description
    gene_id = re.search('GeneID:(\d+)', description).group(1)
    gene_name = description.split(" ")[-1]
    other_description = descriptions_from_csv[gene_id]
    new_description = " ".join([description, other_description])
    record.description = new_description
    if gene_id not in isoforms.keys():
        isoforms[gene_id] = []
    isoforms[gene_id].append(record)

results = []
for gene_id in isoforms:
    longest_isoform = { "record": None, "length": 0 }
    for isoform_record in isoforms[gene_id]:
        current_length = len(isoform_record.seq)
        if current_length > longest_isoform["length"]:
            longest_isoform = { "record": isoform_record, "length": current_length }
    results.append(longest_isoform["record"])

SeqIO.write(results, outpath, "fasta")