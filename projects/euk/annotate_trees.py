#!/usr/bin/python3
from ete3 import Tree
import csv
from os import listdir
import sys
sys.path.insert(0, "/Users/anna/work/code/ngs/")
from py_scripts.helpers.parse_csv import *

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def annotate_tree(tree, info_dict):
    used_names = []
    for leaf in tree.iter_leaves():
        old_name = leaf.name
        id = old_name
        if id in info_dict.keys():
            id_dict = info_dict[id]
            new_name = '_'.join([id, id_dict['Domain'], id_dict['Phylum'], id_dict['Class'], id_dict['Order']])
        else:
            new_name = old_name
        if new_name in used_names:
            print (id, "is duplicated!")
            return (1)
        leaf.name = new_name
        used_names.append(new_name)
    return tree

def annotate_trees(in_treedir, out_treedir, info_path):
    info_dict = csv_to_dict(info_path, main_key="id", delimiter=',')
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file
        tree = Tree(tree_path)
        new_tree = annotate_tree(tree, info_dict)
        new_tree_path = out_treedir + tree_file
        tree.write(format=2, outfile=new_tree_path)
    return 0

in_treedir="/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/constrained_trees/"
out_treedir="/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/annotated_constrained_trees/"
info_path="/Users/anna/work/euk_local/ed_markers/S3_700ArcBac_species_list.csv"

annotate_trees(in_treedir, out_treedir, info_path)
