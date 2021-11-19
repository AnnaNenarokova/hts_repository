#!/usr/bin/python3
from ete3 import Tree
import csv

def csv_to_dict_simple(csv_path, delimiter=','):
    csv_dict = {}
    with open(csv_path) as handle_file:
        handle_csv = csv.reader(handle_file, delimiter=delimiter)
        for row in handle_csv:
            csv_dict[row[0]] = row[1]
        handle_file.close()
    return csv_dict

def rename_trees(treedir, info_path):
	info_dict = csv_to_dict_simple(info_path)
	for tree_name in listdir(treedir_path):
		pass
	return 0

treedir="/Users/anna/work/euk_local/ed_markers/single_gene_trees/"
info_path="/Users/anna/work/euk_local/ed_markers/ids_taxonomy.csv"
csv_dict = csv_to_dict_simple(info_path)
