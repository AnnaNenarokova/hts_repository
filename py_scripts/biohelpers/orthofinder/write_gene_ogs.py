#!python3
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def read_og_file(og_path, gene_delimeter=", "):
    og_dict = csv_to_dict(og_path, "Orthogroup", delimiter='\t')
    for og in og_dict:
        for species in og_dict[og]:
            og_dict[og][species] = og_dict[og][species].split(gene_delimeter)
    return og_dict

def write_gene_ogs(og_path, outpath, species_name):
    og_dict = read_og_file(og_path)
    gene_dict = {}
    for og in og_dict:
        genes = og_dict[og][species_name]
        for gene in genes:
            if gene:
                gene_dict[gene] = og
    write_dict(gene_dict, outpath)
    return outpath

og_path = "/Users/annanenarokova/work/myxo_local/orthofinder/old_orthofinder/Orthogroups.tsv"
outpath = "/Users/annanenarokova/work/myxo_local/orthofinder/old_orthofinder/smol_genes_ogs.tsv"
species_name = "Sphaerospora_molnari_G"

write_gene_ogs(og_path, outpath, species_name)