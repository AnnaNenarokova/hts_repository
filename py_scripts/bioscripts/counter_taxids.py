#!/usr/bin/python
from collections import Counter
from ete3 import NCBITaxa
ncbi = NCBITaxa()
diamond_out_path = "/home/anna/bioinformatics/diplonema/dpapi_genome_diamond.out"
f = open(diamond_out_path, "r")
taxids = []

for line in f:
    newtaxid = line.split("\t")[1]
    taxids.append(newtaxid)

taxid_counter = Counter(taxids)
taxids_nr = taxid_counter.keys()
tax_names = ncbi.get_taxid_translator(taxids_nr)

output = open('taxid_counter.tsv', 'w')
for taxid in taxid_counter:
    taxid_count = taxid_counter[taxid]
    if taxid == "0":
        name = "None"
    else:
        name = tax_names[int(taxid)]
        isBacteria = 1 if 2 in ncbi.get_lineage(taxid) else 0
    output.write('{}\t{}\t{}\t{}\n'.format(taxid, name, taxid_count, isBacteria))
output.close()
