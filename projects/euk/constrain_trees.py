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

def write_constrained_tree_alphabac(alignment, euk_list, alpha_list, outtree):
	seqlist = SeqIO.index(alignment, "fasta")
	seqset = set(seqlist)
	monophyletic_set = set.intersection(set(euk_list + alpha_list), seqset)
	constrained_tree = make_constrained_tree(full_seqset, monophyletic_set