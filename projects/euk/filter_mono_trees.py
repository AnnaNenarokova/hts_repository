#!/usr/bin/python3
import re
from os import listdir
from ete3 import Tree

def listdir_nohidden(path):
	for f in listdir(path):
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
	old_node = target_leaf
	node = old_node
	while check_sisters_tag(node, leaf_tags, group_tag):
		old_node = node
		if node.up:
			node = node.up
		else: 
			return node
	else: return old_node

def get_largest_group_node(tree, leaf_tags, group_tag):
	largest_group_node = []
	for leaf in tree.iter_leaves():
		if leaf not in largest_group_node:
			group_node = get_group_node(leaf, leaf_tags, group_tag=group_tag)
			if len(group_node) > len(largest_group_node):
				largest_group_node = group_node
	return largest_group_node

def filter_mono_tree(tree_path, outpath, group_tag):
	tree = Tree(tree_path)
	leaf_tags = get_tags_leaves_euk(tree)
	group_largest_branch = get_largest_group_node(tree, leaf_tags, group_tag=group_tag)
	group_seqs_kept = []
	group_seqs_out = []
	for leaf in tree.iter_leaves():
		if leaf_tags[leaf.name] == group_tag:
			if leaf in group_largest_branch:
				group_seqs_kept.append(leaf.name)
			else:
				group_seqs_out.append(leaf.name)
	print (tree_path, len(group_seqs_kept), len(group_seqs_out))
	# print (len(group_seqs_kept), group_tag, "seqs kept,", len(group_seqs_out), group_tag, "seqs filtered out")
	with open(outpath, "w") as outfile:
		for seqid in group_seqs_kept:
			outfile.write(seqid)
	return group_seqs_kept

def filter_mono_trees(treedir, outdir, group_tag):
	for tree_file in listdir_nohidden(treedir):
		tree_path = treedir + tree_file
		outpath = outdir + tree_file + "_" +group_tag + ".txt"
		filter_mono_tree(tree_path, outpath, group_tag=group_tag)
	return outdir

treedir = "/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/msa1_LGG/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/singlehit_results/euk_largest_branches/"

filter_mono_trees(treedir, outdir, group_tag="euk")
