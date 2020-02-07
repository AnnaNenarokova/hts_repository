#!python3
from ete3 import Tree
from ete3 import NCBITaxa
import sys
from os import listdir
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

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
        if "DIPPA" in seqid:
            leaf_tags[seqid] = "dpapi"
        elif seqid in tag_dict.keys():
            leaf_tags[seqid] = tag_dict[seqid]
        else:
            # print (seqid, "is not in tag dict!")
            leaf_tags[seqid] = "other"
    return leaf_tags

def check_sisters_tag(node, leaf_tags, tag="bacteria"):
    sister_branches = node.get_sisters()
    if sister_branches:
        for node in sister_branches:
            sister_leaves = node.get_leaves()
            for leaf in sister_leaves:
                if leaf_tags[leaf.name] != tag:
                    return False
    return True

def get_mono_tag_node(in_node, leaf_tags, needed_tag="diplonemid"):
    # bad_tree = False
    # if not bad_tree and in_node.get_leaves()[0].name == "DIPPA_19042.mRNA.1":
    #     bad_tree = True
    sister_branches = in_node.get_sisters()
    for node in sister_branches:
        leaves = node.get_leaves()
        for leaf in leaves:
            leaf_tag = leaf_tags[leaf.name]
            # if bad_tree:
            #     print leaf, leaf_tag
            if leaf_tag != needed_tag:
                return in_node
    result = get_mono_tag_node(in_node.up, leaf_tags, needed_tag="diplonemid")
    return result

def check_hgt(dpapi_leaf, leaf_tags, mode="dpapi"):
    if mode == "dpapi":
        diplo_node = dpapi_leaf
    elif mode == "diplonemid":
        diplo_node = get_mono_tag_node(dpapi_leaf, leaf_tags, needed_tag="diplonemid")
    if check_sisters_tag(diplo_node, leaf_tags, tag="bacteria") and check_sisters_tag(diplo_node.up, leaf_tags, tag="bacteria"):
        return True
    return False

def analyse_tree(tree_path, tag_dict, bootstrap_threshold=70.0, mode="diplonemid"):
    tree = Tree(tree_path)
    tree = remove_bad_nodes(tree, support_threshold=bootstrap_threshold)

    leaf_tags = get_tags_leaves(tree, tag_dict)

    dpapi_leaf = None
    for leaf in tree.iter_leaves():
        if leaf_tags[leaf.name] == "dpapi":
            if not dpapi_leaf:
                dpapi_leaf = leaf
            else:
                print ("More than one Dpapi leaf!\n" + tree_path + "\n")
    if not dpapi_leaf:
        print ("No Dpapi leaf!\n" + tree_path + "\n")
    farthest_node = dpapi_leaf.get_farthest_node(topology_only=True)[0]
    if farthest_node.up == tree:
        result = False
    else:
        tree.set_outgroup(farthest_node.up)
    edited_tree_path = tree_path + "_edited.tree"
    tree.write(outfile=edited_tree_path)

    result = check_hgt(dpapi_leaf, leaf_tags, mode=mode)
    # if result:
    #     print tree
    return result

bootstrap_threshold = 70.0

treedir_path="/home/anna/bioinformatics/diplonema/hgt/results_last/trees/"
tag_path="/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_tags.tsv"

tag_dict = parse_tags(tag_path)
i = 0
for tree_name in listdir(treedir_path):
    tree_path = treedir_path + tree_name
    # if i == 5:
    #     break
    is_hgt = analyse_tree(tree_path, tag_dict, bootstrap_threshold=bootstrap_threshold, mode = "diplonemid")
    if is_hgt:
        i += 1
        print "hgt", tree_name
