#!python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def make_constrained_tree(full_seqset, monophyletic_set):
	other_set = full_seqset - monophyletic_set
	monophyletic_clade = "(" + ",".join(monophyletic_set) + ")"
	full_tree_set = monophyletic_clade + other_set
	constrained_tree = "(" + ",".join(full_tree_set) + ");"
	return constrained_tree

def write_constrained_tree_mono(alignment, list1, list2, outtree_path):
	seqlist = SeqIO.index(alignment, "fasta")
	seqset = set(seqlist)
	monophyletic_set = set.intersection(set(list1 + list2), seqset)
	constrained_tree = make_constrained_tree(full_seqset, monophyletic_set)
	return outtree_path

def constrain_trees(msa_dir, list1_path, list2_path, outdir):
	return 0