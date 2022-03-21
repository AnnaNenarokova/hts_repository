#!python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def make_constrained_tree(seqlist, list1, list2):
	seqset = set(seqlist)
	monophyletic_set = set.intersection(set(list1 + list2), seqset)
	other_set = seqset - monophyletic_set
	monophyletic_clade = "(" + ",".join(monophyletic_set) + ")"
	full_tree_set = other_set
	full_tree_set.update(set(monophyletic_clade))
	constrained_tree = "(" + ",".join(full_tree_set) + ");"
	return constrained_tree

def read_list(list_path):
	result_list = []
	with open (list_path) as list_file:
		for line in list_file:
			result_list.append(line.rstrip())
	return result_list

def constrain_trees(msa_dir, list1_path, list2_dir, outdir):
	for msa in listdir_nohidden(msa_dir):
		print (msa)
		msa_path = msa_dir + msa
		seqlist = SeqIO.index(msa_path, "fasta")
		name = msa.split(".")[0]

		list1 = read_list(list1_path)
		list2_path = list2_dir + name + ".txt"
		list2 = read_list(list2_path)

		outtree_path = outdir + name + ".tree"
		constrained_tree = make_constrained_tree(seqlist, list1, list2)
		with open (outtree_path, "w") as outtree_file:
			outtree_file.write(constrained_tree)
	return 0

msa_dir = "/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/msa/"
alpha_list = "/Users/anna/work/code/ngs/projects/euk/alpha_list_ed.txt"
euk_lists_dir = "/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/alphabac_euk_lists/"
outdir = "/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/constrained_trees/"

constrain_trees(msa_dir, alpha_list, euk_lists_dir, outdir)