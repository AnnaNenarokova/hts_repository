#!python3
from ete3 import NCBITaxa
from ete3 import Tree

taxid_filepath = "/home/vl18625/bioinformatics/diplonema/hgt/all_seqids_taxids.csv"
tree_path = "/home/vl18625/bioinformatics/diplonema/hgt/results/trees_copy/DIPPA_01494.mRNA.1.faa_trimmed_msa.fasta.treefile.tree"
bootstrap_threshold = 70.0

def parse_taxids(taxid_filepath, delimeter=","):
    taxid_dict = {}
    with open(taxid_filepath) as taxid_file:
        for line in taxid_file:
            line_split = line.rstrip().split(delimeter)
            seqid = line_split[0]
            taxid = line_split[1]
            taxid_dict[seqid] = taxid
    return taxid_dict

def remove_bad_nodes(tree, support_threshold=70.0):
    for node in tree.traverse(strategy='postorder'):
        if (not node.is_leaf() and node.support < support_threshold):
            node.delete()
    return tree

def check_sisters_bacteria(node, leaf_tags):
    sisters = node.get_sisters()
    all_sisters_bacteria = True
    for node in sisters:
        if node.is_leaf() and (leaf_tags[leaf] != "bacteria"):
            all_sisters_bacteria = False
    return all_sisters_bacteria

taxid_dict = parse_taxids(taxid_filepath)

tree = Tree(tree_path)

polytomic_tree_path = tree_path + "_polytomic.tree"
tree = remove_bad_nodes(tree, support_threshold=bootstrap_threshold)
tree.write(outfile=polytomic_tree_path)

leaf_tags = get_tags_leaves(tree, taxid_dict)

dpapi_leaf = None
for leaf in tree.iter_leaves():
    if leaf_tags[leaf] == "dpapi":
        if not dpapi_leaf:
            dpapi_leaf = leaf
        else:
            print ("More than one Dpapi leaf!\n" + tree_path + "\n")