#!/usr/bin/python3
from Bio import Phylo
# Read the tree from a Newick file
tree_path = "/Users/vl18625/work/euk/benoit_toy_mcmctree/mcmctree/short_names_2cyanos_branch_len.tree"
tree = Phylo.read(tree_path, "newick")

# Get the maximum height of the tree
tree_height = max(clade.branch_length for clade in tree.get_terminals())

root_age = 39.335 # in 100 Mya

mean_rate = tree_height / root_age

alpha = 2

beta = alpha / mean_rate

print (alpha, beta)