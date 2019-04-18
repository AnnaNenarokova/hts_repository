#!python3
from ete3 import NCBITaxa
from ete3 import Tree
import sys 
from os import listdir

treedir_path="/projects/Diplonema_genome_evolution/hgt/results/trees/"
taxid_path="/projects/Diplonema_genome_evolution/hgt/wholedataset_1_taxid.csv"
bootstrap_threshold = 70.0

def parse_taxids(taxid_path, delimeter=","):
    taxid_dict = {}
    with open(taxid_path) as taxid_file:
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

def get_tags_leaves(tree, taxid_dict):
    ncbi_taxa = NCBITaxa()
    bacteria_taxid = 2
    dpapi_taxid = 91374
    leaf_tags = {}
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if "DIPPA" in seqid:
            leaf_tags[seqid] = "dpapi"
        else:
            print (seqid)
            print (taxid_dict[seqid])
            taxid = int(taxid_dict[seqid])
            if taxid == dpapi_taxid:
                leaf_tags[seqid] = "dpapi"
            elif bacteria_taxid in ncbi_taxa.get_lineage(taxid):
                leaf_tags[seqid] = "bacteria"
            else:
                leaf_tags[seqid] = "other"
    return leaf_tags

def check_sisters_bacteria(node, leaf_tags):
    sister_branches = node.get_sisters()
    for node in sister_branches:
        sister_leaves = node.get_leaves()
        for leaf in sister_leaves:
            if leaf_tags[leaf.name] != "bacteria":
                return False
    return True

def check_hgt(tree_path, taxid_dict, bootstrap_threshold=70.0):

    tree = Tree(tree_path)
    tree = remove_bad_nodes(tree, support_threshold=bootstrap_threshold)

    leaf_tags = get_tags_leaves(tree, taxid_dict)

    dpapi_leaf = None
    for leaf in tree.iter_leaves():
        if leaf_tags[leaf.name] == "dpapi":
            if not dpapi_leaf:
                dpapi_leaf = leaf
            else:
                print ("More than one Dpapi leaf!\n" + tree_path + "\n")

    farthest_node = dpapi_leaf.get_farthest_node(topology_only=True)[0]
    tree.set_outgroup(farthest_node.up)

    edited_tree_path = tree_path + "_edited.tree"
    tree.write(outfile=edited_tree_path)

    if check_sisters_bacteria(dpapi_leaf, leaf_tags) and check_sisters_bacteria(dpapi_leaf.up, leaf_tags):
        return True
    else:
        return False

taxid_dict = parse_taxids(taxid_path)
for tree in listdir(treedir_path):
    tree_path = treedir_path + tree
    print ("@", tree)
    is_hgt = check_hgt(tree_path, taxid_dict, bootstrap_threshold=bootstrap_threshold)
    print (tree, is_hgt)