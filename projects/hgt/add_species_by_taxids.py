#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from ete3 import NCBITaxa
ncbi = NCBITaxa()

def add_species_by_taxids(input, output):
    delimiter = ","
    n_column_taxid = 3
    n_column_taxid = n_column_taxid - 1
    taxids = []
    with open(input_path) as input_f:
        for line in input_f:
            line_split = line.rstrip().split(delimiter)
            taxid = line_split[n_column_taxid]
            if taxid.isdigit():
                taxids.append(taxid)
    taxids_nr = list(set(taxids))
    tax_names = ncbi.get_taxid_translator(taxids_nr)
    tax_ranks = ncbi.get_rank(taxids_nr)
    with open(input_path) as input_f, open(output_path,"w") as output_f:
        i = 0
        for line in input_f:
            i += 1
            print (i)
            line_split = line.rstrip().split(delimiter)
            taxid = line_split[n_column_taxid]
            tax_name = "taxid_name"
            rank = "rank"
            if taxid.isdigit():
                taxid = int(taxid)
                if taxid == 0:
                    tax_name = ""
                    rank = ""
                else:
                    tax_name = tax_names[taxid]
                    rank = tax_ranks[taxid]
            else:
                tax_name = ""
                rank = ""
            outline = line[:-1] + delimiter + tax_name + delimiter + rank + "\n"
            output_f.write(outline)

input_path = "/home/anna/bioinformatics/novymonas/assembly_diamond_nr.csv"
output_path = "/home/anna/bioinformatics/novymonas/assembly_diamond_nr_sps.csv"

add_species_by_taxids(input_path, output_path)
