#!python3
from ete3 import Tree
import sys
from os import listdir

def parse_tags(tag_path, delimeter="\t"):
    tag_dict = {}
    with open(tag_path) as tag_file:
        for line in tag_file:
            seqid, tag =  line.rstrip().split(delimeter)
            tag_dict[seqid] = tag
    return tag_dict

def remove_bad_nodes(tree, support_threshold=70.0):
    for node in tree.traverse(strategy='postorder'):
        if (not node.is_leaf() and node.support < support_threshold):
            node.delete()
    return tree

def get_tags_leaves(tree, tag_dict):
    leaf_tags = {}
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if seqid in tag_dict.keys():
            leaf_tags[seqid] = tag_dict[seqid]
        else:
            print (seqid, "is not in tag dict!")
            leaf_tags[seqid] = "other"
    return leaf_tags

def get_mono_tag_node(in_node, leaf_tags, needed_tag="Diplonemea"):
    sister_branches = in_node.get_sisters()
    for node in sister_branches:
        leaves = node.get_leaves()
        for leaf in leaves:
            leaf_tag = leaf_tags[leaf.name]
            if leaf_tag != needed_tag:
                return in_node
    result = get_mono_tag_node(in_node.up, leaf_tags, needed_tag=needed_tag)
    return result

def check_sisters_tag(node, leaf_tags, tag):
    sister_branches = node.get_sisters()
    if sister_branches:
        for node in sister_branches:
            sister_leaves = node.get_leaves()
            for leaf in sister_leaves:
                if leaf_tags[leaf.name] != tag:
                    return False
    return True

def analyse_tree(tree_path, tag_dict, bootstrap_threshold=70.0):
    result = None
    tree = Tree(tree_path)
    tree_name = tree_path.split("/")[-1].split(".")[0]
    dpapi_name = tree_name
    leaf_tags = get_tags_leaves(tree, tag_dict)
    edited_tree = remove_bad_nodes(tree, support_threshold=bootstrap_threshold)

    dpapi_leaf = None
    for leaf in edited_tree.iter_leaves():
        if leaf.name == dpapi_name:
            if not dpapi_leaf:
                dpapi_leaf = leaf
            else:
                print ("More than one Dpapi leaf!\n" + tree_path + "\n")
    if not dpapi_leaf:
        print ("No Dpapi leaf!\n" + tree_path + "\n")
        return result

    farthest_node = dpapi_leaf.get_farthest_node(topology_only=True)[0]
    if farthest_node.up == edited_tree:
        result = False
        return result
    else:
        tree.set_outgroup(farthest_node.up)
    diplo_node = get_mono_tag_node(dpapi_leaf, leaf_tags, needed_tag="Diplonemea")
    if check_sisters_tag(diplo_node, leaf_tags, tag="Bacteria") and check_sisters_tag(diplo_node.up, leaf_tags, tag="Bacteria"):
        result = True
        return result
    result = False
    return result

bootstrap_threshold = 70.0

treedir_path="/Users/annanenarokova/work/dpapi_local/results/trees2/"
tag_path="/Users/annanenarokova/work/dpapi_local/seqs_tags.tsv"

tag_dict = parse_tags(tag_path, delimeter="\t")

for tree_name in listdir(treedir_path):
    tree_path = treedir_path + tree_name
    is_hgt = analyse_tree(tree_path, tag_dict, bootstrap_threshold=bootstrap_threshold)
    if is_hgt:
        print (tree_name, "HGT", is_hgt)
