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
    diplo_ids = []
    tree = Tree(tree_path)
    query_name = tree_path.split("/")[-1].split(".")[0]
    leaf_tags = get_tags_leaves(tree, tag_dict)
    edited_tree = remove_bad_nodes(tree, support_threshold=bootstrap_threshold)
    dpapi_leaf = None

    for leaf in edited_tree.iter_leaves():
        if leaf.name == query_name:
            if not dpapi_leaf:
                dpapi_leaf = leaf
            else:
                print ("More than one query_name leaf!\n" + tree_path + "\n")
    if not dpapi_leaf:
        print ("No query_name leaf!\n" + tree_path + "\n")
        for leaf in edited_tree.iter_leaves():
            if "Diplonema-papillatum" in leaf.name:
                dpapi_leaf = leaf

    if not dpapi_leaf:
        print ("No D. papi leaf!\n" + tree_path + "\n")
        return result, diplo_ids

    farthest_node = dpapi_leaf.get_farthest_node(topology_only=True)[0]
    if farthest_node.up == edited_tree:
        result = False
        return result, diplo_ids
    else:
        tree.set_outgroup(farthest_node.up)
    diplo_node = get_mono_tag_node(dpapi_leaf, leaf_tags, needed_tag="Diplonemea")
    if check_sisters_tag(diplo_node, leaf_tags, tag="Bacteria") and check_sisters_tag(diplo_node.up, leaf_tags, tag="Bacteria"):
        result = True
        for leaf in diplo_node.get_leaves():
            diplo_ids.append(leaf.name)
    else:
        result = False
    return result, diplo_ids

def analyse_trees(treedir_path, tag_path, outdir, bootstrap_threshold=70.0):
    tag_dict = parse_tags(tag_path, delimeter="\t")
    hgt_result_path = outdir + "hgt_result.tsv"
    hgt_dict = {}
    with open(hgt_result_path, "w") as hgt_result:
        hgt_result.write("gene_id\tis_hgt\n")
        for tree_name in listdir(treedir_path):
            tree_path = treedir_path + tree_name
            current_dpapi_id = tree_name.split(".")[0]
            try:
                is_hgt, diplo_ids = analyse_tree(tree_path, tag_dict, bootstrap_threshold=bootstrap_threshold)
                hgt_result.write(current_dpapi_id + "\t" + str(is_hgt) + "\n")
                if is_hgt:
                    in_dict = False
                    for dpapi_id in hgt_dict:
                        if current_dpapi_id in hgt_dict[dpapi_id]:
                            in_dict = True
                            hgt_dict[dpapi_id].update(diplo_ids)
                            break
                    if not in_dict:
                        hgt_dict[current_dpapi_id] = set(diplo_ids)       
            except:
                print (tree_name, "Error!")
                result = analyse_tree(tree_path, tag_dict, bootstrap_threshold=bootstrap_threshold)
                print (result)
    return hgt_dict

def analyse_hgt_dict(hgt_dict, outdir):
    hgt_ids_path = outdir + "hgt_ids.tsv"
    hgt_ids_dpapi_path = outdir + "hgt_dpapi_only_ids.tsv"
    hgt_group_result_path = outdir + "hgt_group_result.tsv"
    with open(hgt_ids_path, "w") as hgt_ids, open(hgt_ids_dpapi_path,"w") as hgt_ids_dpapi, open(hgt_group_result_path,"w") as hgt_group_result:
        hgt_ids.write("hgt_id_group\tgene_id\n")
        hgt_ids_dpapi.write("hgt_id_group\tgene_id\n")
        hgt_group_result.write("hgt_id_group\tonly_dpapi\n")
        for dpapi_id in hgt_dict:
            non_dpapi_seq = False
            for id in hgt_dict[dpapi_id]:
                hgt_ids.write(dpapi_id + "\t" + id + "\n")
                if "Diplonema-papillatum" in id:
                    hgt_ids_dpapi.write(dpapi_id + "\t" + id + "\n")
                else:
                    non_dpapi_seq = True
            if non_dpapi_seq:
                group_result = False
            else:
                group_result = True
            hgt_group_result.write(dpapi_id + "\t" + str(group_result) + "\n")
    return 0

treedir_path="/Users/annanenarokova/work/dpapi_local/results_16_08/trees/"
tag_path="/Users/annanenarokova/work/dpapi_local/results_16_08/all_tags.tsv"
outdir="/Users/annanenarokova/work/dpapi_local/results_16_08/"
hgt_dict = analyse_trees(treedir_path, tag_path, outdir)
analyse_hgt_dict(hgt_dict, outdir)

