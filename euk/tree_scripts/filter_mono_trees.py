#!/usr/bin/python3
import re
from os import listdir
from ete3 import Tree

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def get_tags_leaves_eukprot(tree):
	euk_regex = "^EP\d+-P\d+"
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
	else: return node

def get_largest_group_node(tree, leaf_tags, group_tag):
	largest_group_node = []
	for leaf in tree.iter_leaves():
		if (leaf_tags[leaf.name] == group_tag) and (leaf not in largest_group_node):
			group_node = get_group_node(leaf, leaf_tags, group_tag=group_tag)
			if len(group_node) > len(largest_group_node):
				largest_group_node = group_node
	return largest_group_node

def filter_mono_tree(tree_path, outpath, group_tag):
	tree = Tree(tree_path)
	leaf_tags = get_tags_leaves_eukprot(tree)
	for leaf in tree.iter_leaves():
		if leaf_tags[leaf.name] != group_tag:
			tree.set_outgroup(leaf)
			break
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
	outpath_in = outpath + "_in.txt"
	outpath_out = outpath + "_out.txt"
	with open(outpath_in, "w") as outfile:
		for seqid in group_seqs_kept:
			outfile.write(seqid + "\n")
	with open(outpath_out, "w") as outfile:
		for seqid in group_seqs_out:
			outfile.write(seqid + "\n")
	return group_seqs_kept

def filter_mono_trees(treedir, outdir, group_tag):
	for tree_file in listdir_nohidden(treedir):
		tree_path = treedir + tree_file
		outpath = outdir + tree_file + "_" + group_tag
		filter_mono_tree(tree_path, outpath, group_tag=group_tag)
	return outdir

treedir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be/c20_trees/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be/euk_c20_alpha_monobranch/"
filter_mono_trees(treedir, outdir, group_tag="euk")