#!/usr/bin/python3
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
