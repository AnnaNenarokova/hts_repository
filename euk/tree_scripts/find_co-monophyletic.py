#!/usr/bin/python3
import re
from os import listdir
from ete3 import Tree

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def get_tags_leaves_eukprot_two_groups(tree, gid_list, delimiter="-"):
	euk_regex = "^EP\d+-P\d+"
	leaf_tags = {}
	for leaf in tree.iter_leaves():
		seqid = leaf.name
		genome_id = seqid.split(delimiter)[0]
		if re.match(euk_regex, seqid):
			leaf_tags[seqid] = "euk_group"
		elif genome_id in gid_list:
			leaf_tags[seqid] = "euk_group"
		else:
			leaf_tags[seqid] = "other"
	return leaf_tags

def get_full_tags_leaves_eukprot(tree, gid_list, delimiter="-"):
	euk_regex = "^EP\d+-P\d+"
	leaf_tags = {}
	for leaf in tree.iter_leaves():
		seqid = leaf.name
		genome_id = seqid.split(delimiter)[0]
		if re.match(euk_regex, seqid):
			leaf_tags[seqid] = "euk"
		elif genome_id in gid_list:
			leaf_tags[seqid] = "bact_outgroup"
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

def check_sisters_not_tag(node, leaf_tags, tag):
	sister_branches = node.get_sisters()
	if sister_branches:
		for node in sister_branches:
			sister_leaves = node.get_leaves()
			for leaf in sister_leaves:
				if leaf_tags[leaf.name] == tag:
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

def check_group_node(group_node, full_tags, tag_of_interest):
	result = False
	for leaf in group_node.iter_leaves():
		if full_tags[leaf.name] == tag_of_interest:
			result = True
			break
	return result

def get_largest_group_node(tree, leaf_tags, full_tags, group_tag, tag_of_interest="bact_outgroup"):
	largest_group_node = []
	for leaf in tree.iter_leaves():
		if (leaf_tags[leaf.name] == group_tag) and (leaf not in largest_group_node):
			group_node = get_group_node(leaf, leaf_tags, group_tag=group_tag)
			if len(group_node) > len(largest_group_node) and check_group_node(group_node, full_tags, tag_of_interest):
				largest_group_node = group_node
	return largest_group_node

def filter_mono_tree(tree_path, outpath, gid_list, group_tag="euk_group"):
	tree = Tree(tree_path)
	leaf_tags = get_tags_leaves_eukprot_two_groups(tree, gid_list, delimiter="-")
	full_tags = get_full_tags_leaves_eukprot(tree, gid_list, delimiter="-")

	for leaf in tree.iter_leaves():
		if leaf_tags[leaf.name] != group_tag:
			tree.set_outgroup(leaf)
			break
	group_largest_branch = get_largest_group_node(tree, leaf_tags, full_tags, group_tag, tag_of_interest="bact_outgroup")

	tree_name = tree_path.split("/")[-1].split(".faa.treefile")[0]

	seqs_in_monobranch = 0
	seqs_out_monobranch = 0
	euks_in = 0
	euks_out = 0
	group_in = 0
	group_out = 0
	other_out = 0
	total_seqs = 0
	for leaf in tree.iter_leaves():
		total_seqs += 1
		if leaf in group_largest_branch:
			seqs_in_monobranch += 1
			if full_tags[leaf.name] == "euk":
				euks_in += 1
			elif full_tags[leaf.name] == "bact_outgroup":
				group_in += 1
			else:
				print ("Error in ", leaf.name)
		else:
			seqs_out_monobranch += 1
			if full_tags[leaf.name] == "euk":
				euks_out += 1
			elif full_tags[leaf.name] == "bact_outgroup":
				group_out += 1
			else:
				other_out += 1
			
	print (tree_name, seqs_in_monobranch, group_in, euks_in, seqs_out_monobranch, group_out, euks_out, other_out, total_seqs)
	return 0 

def filter_mono_trees(treedir, outdir, gid_list, group_tag="euk_group"):
	print ("tree_name seqs_in group_in euk_in seqs_out group_out euk_out other_out total_seqs")
	for tree_file in listdir_nohidden(treedir):
		tree_path = treedir + tree_file
		outpath = outdir + tree_file + "_" + group_tag
		filter_mono_tree(tree_path, outpath, gid_list, group_tag=group_tag)
	return outdir

alpha_proteo_list=["GCA_002422845.1","GCA_009780035.1","GCA_006738645.1","GCA_002117145.1","GCA_000144605.1","GCA_000013025.1","GCA_000152825.2","GCA_007197755.1","GCA_002717245.1","GCA_002722055.1","GCA_002746255.1","GCA_000427665.1","GCA_002937855.1","GCA_001898075.1","GCA_000742475.1","GCA_000469665.2","GCA_000515255.1","GCA_000226315.1","GCA_004210305.1","GCA_000293845.2","GCA_000012345.1","GCA_000163555.2","GCA_900167455.1","GCA_902799835.1","GCA_000021745.1","GCA_000143145.1","GCA_000192745.1","GCA_000155675.2","GCA_003324715.1","GCA_003970735.1","GCA_002938315.1","GCA_000013085.1","GCA_003403095.1","GCA_000746585.2","GCA_000166935.1","GCA_002787635.1","GCA_002291925.1","GCA_009784235.1","GCA_000616095.1","GCA_002722885.1","GCA_000375545.1","GCA_000186705.2","GCA_009768975.1","GCA_000299935.1","GCA_000264455.2","GCA_002937655.1","GCA_002937675.1","GCA_002937625.1","GCA_002691145.1","GCA_002937495.1","GCA_002422365.1","GCA_002436405.1","GCA_001767855.1","GCA_002728255.1","GCA_011523425.1"]
cyano_list=["GCA_000464785.1","GCA_003503675.1","GCA_000155555.1","GCA_000019485.1","GCA_000346485.2","GCA_000204075.1","GCA_000484535.1","GCA_001870225.1","GCA_000353285.1","GCA_000015645.1","GCA_000195975.1","GCA_000013225.1","GCA_002075285.3","GCA_000317065.1","GCA_000010065.1","GCA_000018105.1","GCA_003149375.1"]

treedir = "/Users/anna/work/euk_local/nina_markers/singlehit_results/alpha/be/treefiles/"
outdir = ""
# filter_mono_trees(treedir, outdir, alpha_proteo_list, group_tag="euk_group")


treedir="/Users/anna/work/euk_local/nina_markers/singlehit_results/cyano/treefiles/"
filter_mono_trees(treedir, outdir, cyano_list, group_tag="euk_group")

# tree_path = "/Users/anna/work/euk_local/nina_markers/singlehit_results/cyano/treefiles/COG0037.faa.treefile"
# gid_list = cyano_list
# outpath = ""
# filter_mono_tree(tree_path, outpath, gid_list, group_tag="euk_group")