#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def make_og_eggnog_dict(eggnog_dict, gene_og_dict):
    og_dict = {}
    for gene in gene_og_dict:
        if gene in eggnog_dict:
            og = gene_og_dict[gene]
            if og not in og_dict:
                og_dict[og] = {}
            og_dict[og][gene] = eggnog_dict[gene]
    return og_dict

def choose_best_kegg(og_annotation_dict, key="KEGG_ko"):
    best_kegg_ko = None
    best_evalue = 10.0
    for gene in og_annotation_dict:
        evalue = float(og_annotation_dict[gene]['seed_ortholog_evalue'])
        kegg_ko = og_annotation_dict[gene][key]
        if evalue < best_evalue:
            best_kegg_ko = kegg_ko
    return best_kegg_ko

def add_best_eggnog_annotations_ogs(gene_og_path, eggnog_result_path):
    eggnog_dict = csv_to_dict(eggnog_result_path, main_key="query_name", delimiter='\t')
    gene_og_dict = csv_to_dict_simple(gene_og_path)
    og_eggnog_dict = make_og_eggnog_dict(eggnog_dict, gene_og_dict)
    result_dict = {}
    for og in og_eggnog_dict:
        best_kegg_ko = choose_best_kegg(og_eggnog_dict[og], key='BRITE')
        result_dict[og] = best_kegg_ko
    return result_dict

eggnog_result_path = "/Users/annanenarokova/work/myxo_local/eggnog.tsv"
gene_og_path = "/Users/annanenarokova/work/myxo_local/orthofinder/old_orthofinder/smol_genes_ogs.tsv"
outpath = "/Users/annanenarokova/work/myxo_local/orthofinder/old_orthofinder/ogs_kegg_brite.tsv"

result_dict = add_best_eggnog_annotations_ogs(gene_og_path, eggnog_result_path)

write_dict(result_dict, outpath, delimiter="\t")