#!/usr/bin/python3
import re
from os import listdir
from ete3 import Tree

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def get_tags_leaves_euk(tree):
	euk_regex = "^EP\d+_P\d+"
    leaf_tags = {}
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if re.match(euk_regex, seqid):
        	leaf_tags[seqid] = "euk"
        else:
        	leaf_tags[seqid] = "other"
    return leaf_tags

def check_sisters_tag(node, leaf_tags, tag):
    sister_branches = node.get_sisters()
    if sister_branches:
        for node in sister_branches:
            sister_leaves = node.get_leaves()
            for leaf in sister_leaves:
                if leaf_tags[leaf.name] != tag:
                    return False
    return True

def get_group_node(target_leaf, leaf_tags, group_tag):
    node = target_leaf
    while check_sisters_tag(node, leaf_tags, group_tag):
        if node.up:
            node = node.up
        else: 
            return node
    return node

def identify_euk_largest_branch(tree):

	return euk_largest_branch

def filter_arch_tree(tree_path, outpath):
	euk_seqs_kept = 0
	euk_seqs_filtered = 0
	tree = Tree(tree_path)
	leaf_tags = get_tags_leaves_eukprot(tree)
	euk_largest_branch = identify_euk_largest_branch(tree)
	print (euk_seqs_kept, "euk seqs kept,", euk_seqs_filtered, "euk seqs filtered out")
	return seq_cleaned_list

def filter_arch_trees(treedir, outdir):
	for tree_file in listdir_nohidden(treedir):
		tree_path = treedir + tree_file
		outpath = outdir + tree_file
		filter_arch_tree(tree_path, outpath)
	return outdir