#!/usr/bin/python3
from ete3 import Tree
import csv
from os import listdir

def csv_to_dict_simple(csv_path, delimiter=','):
    csv_dict = {}
    with open(csv_path) as handle_file:
        handle_csv = csv.reader(handle_file, delimiter=delimiter)
        for row in handle_csv:
            csv_dict[row[0]] = row[1]
        handle_file.close()
    return csv_dict

def rename_trees(treedir, name_info_path):
    name_dict = csv_to_dict_simple(name_info_path)
    for tree_file in listdir(treedir):
        tree_path = treedir + tree_file
        tree = Tree(tree_path)
        used_names = []
        for leaf in tree.iter_leaves():
            old_name = leaf.name
            if old_name in name_dict:
                new_name = name_dict[old_name].split("")
                leaf.name = new_name
        new_tree_path = treedir + tree_file + "_renamed"
        tree.write(format=1, outfile=new_tree_path)
    return 0

treedir="/home/anna/work/euk_local/ed_markers_and_euks/single_gene_trees/"
name_info_path="/home/anna/work/euk_local/ed_markers_and_euks/ids_taxonomy.csv"

rename_trees(treedir, name_info_path)
