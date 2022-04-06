#!/usr/bin/python3
from ete3 import Tree
import csv
from os import listdir
from py_scripts.helpers.parse_csv import *

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f


def annotate_trees(treedir, name_info_path):
    name_dict = csv_to_dict_simple(name_info_path)
    for tree_file in listdir_nohidden(treedir):
        tree_path = treedir + tree_file
        tree = Tree(tree_path)
        used_names = []
        for leaf in tree.iter_leaves():
            old_name = leaf.name
            if old_name in name_dict:
                lineage = name_dict[old_name]
                new_name = lineage
                while new_name in used_names:
                    new_name = new_name + "_1"
                leaf.name = new_name
                used_names.append(new_name)
        new_tree_path = treedir + tree_file + "_renamed"
        tree.write(format=2, outfile=new_tree_path)
    return 0

treedir="/Users/anna/work/euk_local/ed_markers/single_gene_trees/"
name_info_path="/Users/anna/work/euk_local/ed_markers/ids_taxonomy.csv"

rename_trees(treedir, name_info_path)
