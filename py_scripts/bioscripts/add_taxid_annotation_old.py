#!/usr/bin/python3
from ete3 import NCBITaxa

ncbi = NCBITaxa()
diamond_path = "/home/anna/bioinformatics/diplonema/dpapi_genome_diamond.tsv"
out_path = "/home/anna/bioinformatics/diplonema/dpapi_genome_diamond_annotation.tsv"

taxids = []

with open(diamond_path) as input_f:
    for line in input_f:
        newtaxid = line.split("\t")[1]
        taxids.append(newtaxid)

taxids_nr = list(set(taxids))
tax_names = ncbi.get_taxid_translator(taxids_nr)

input_f = open(diamond_path, "r")
output_f = open(out_path, 'w')

for line in input_f:
    line_split = line.rstrip().split("\t")
    id = line_split[0]
    taxid = line_split[1]
    evalue = line_split[2]
    if taxid == "0":
        name = "None"
        is_bacteria = 0
    else:
        name = tax_names[int(taxid)]
        is_bacteria = 1 if 2 in ncbi.get_lineage(taxid) else 0

    output_f.write('{}\t{}\t{}\t{}\t{}\n'.format(id, taxid, evalue, name, is_bacteria))

input_f.close()
output_f.close()
