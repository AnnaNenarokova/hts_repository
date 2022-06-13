#!/usr/bin/python3
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
			leaf_tags[seqid] = "mono_branch"
		elif genome_id in gid_list:
			leaf_tags[seqid] = "mono_branch"
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

def get_largest_group_node(tree, leaf_tags, group_tag):
	largest_group_node = []
	for leaf in tree.iter_leaves():
		if (leaf_tags[leaf.name] == group_tag) and (leaf not in largest_group_node):
			group_node = get_group_node(leaf, leaf_tags, group_tag=group_tag)
			if len(group_node) > len(largest_group_node):
				largest_group_node = group_node
	return largest_group_node

def filter_mono_tree(tree_path, outpath, gid_list, group_tag="mono_branch"):
	tree = Tree(tree_path)
	leaf_tags = get_tags_leaves_eukprot_two_groups(tree, gid_list, delimiter="-")
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

def filter_mono_trees(treedir, outdir, gid_list, group_tag="mono_branch"):
	for tree_file in listdir_nohidden(treedir):
		tree_path = treedir + tree_file
		outpath = outdir + tree_file + "_" + group_tag
		filter_mono_tree(tree_path, outpath, group_tag=group_tag)
	return outdir



alpha_proteo_list=["GCA_002422845.1","GCA_009780035.1","GCA_006738645.1","GCA_002117145.1","GCA_000144605.1","GCA_000013025.1","GCA_000152825.2","GCA_007197755.1","GCA_002717245.1","GCA_002722055.1","GCA_002746255.1","GCA_000427665.1","GCA_002937855.1","GCA_001898075.1","GCA_000742475.1","GCA_000469665.2","GCA_000515255.1","GCA_000226315.1","GCA_004210305.1","GCA_000293845.2","GCA_000012345.1","GCA_000163555.2","GCA_900167455.1","GCA_902799835.1","GCA_000021745.1","GCA_000143145.1","GCA_000192745.1","GCA_000155675.2","GCA_003324715.1","GCA_003970735.1","GCA_002938315.1","GCA_000013085.1","GCA_003403095.1","GCA_000746585.2","GCA_000166935.1","GCA_002787635.1","GCA_002291925.1","GCA_009784235.1","GCA_000616095.1","GCA_002722885.1","GCA_000375545.1","GCA_000186705.2","GCA_009768975.1","GCA_000299935.1","GCA_000264455.2","GCA_002937655.1","GCA_002937675.1","GCA_002937625.1","GCA_002691145.1","GCA_002937495.1","GCA_002422365.1","GCA_002436405.1","GCA_001767855.1","GCA_002728255.1","GCA_011523425.1"]
cyano_list=["GCA_000464785.1","GCA_003503675.1","GCA_000155555.1","GCA_000019485.1","GCA_000346485.2","GCA_000204075.1","GCA_000484535.1","GCA_001870225.1","GCA_000353285.1","GCA_000015645.1","GCA_000195975.1","GCA_000013225.1","GCA_002075285.3","GCA_000317065.1","GCA_000010065.1","GCA_000018105.1","GCA_003149375.1"]

treedir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be_mono_results/alpha/treefiles/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be_mono_results/alpha/euk_mono_branch/"
filter_mono_trees(treedir, outdir, group_tag="euk")