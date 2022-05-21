#!python3
import re
from ete3 import Tree
import sys
from os import listdir
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def remove_bad_nodes(tree, support_threshold=70.0):
    for node in tree.traverse(strategy='postorder'):
        if (not node.is_leaf() and node.support < support_threshold):
            node.delete()
    return tree

def get_lineage(seqid):
    ncbi_xml_record = Entrez.efetch(db="protein", id=seqid, retmode="xml").read()
    ncbi_dict = XML2Dict().parse(ncbi_xml_record)
    lineage = ncbi_dict['GBSet']['GBSeq']['GBSeq_taxonomy']
    try:
        lineage = lineage.decode("utf-8")
    except:
        lineage = lineage
    return lineage

def get_lineages_bulk(seqids):
    ncbi_xml_record = Entrez.efetch(db="protein", id=seqids, retmode="xml").read()
    ncbi_dict = XML2Dict().parse(ncbi_xml_record)
    records = ncbi_dict['GBSet']['GBSeq']
    lineages = {}
    for record in records:
        name = record['GBSeq_accession-version']
        lineage = record['GBSeq_taxonomy']

        try:
            lineage = lineage.decode("utf-8")
        except:
            lineage = lineage

        try:
            name = name.decode("utf-8")
        except:
            name = name
        lineages[name] = lineage
    return lineages

def get_tags_leaves_smol(tree, tax_names):
    smol_regex = "^g\d+\.t1"
    leaf_tags = {}
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if re.match(smol_regex, seqid):
            leaf_tags[seqid] = "smol"
        else:
            leaf_tags[seqid] = "other"
    return leaf_tags
    
def get_tags_leaves_myxo_old(tree, tax_names):
    leaf_tags = {}
    smol_regex = "^g\d+\.t1"
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if re.match(smol_regex, seqid):
            leaf_tags[seqid] = "smol"
        else:
            lineage = get_lineage(seqid)
            for tax_name in tax_names:
                if tax_name in lineage:
                    leaf_tags[seqid] = tax_name
                else:
                    leaf_tags[seqid] = "other"

    return leaf_tags

def get_tags_leaves(tree, tax_names):
    leaf_tags = {}
    smol_regex = "^g\d+\.t1"
    ncbi_seqids = []
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if re.match(smol_regex, seqid):
            leaf_tags[seqid] = "smol"
        else:
            ncbi_seqids.append(seqid)

    lineages = get_lineages_bulk(ncbi_seqids)
           
    for leaf in tree.iter_leaves():
        seqid = leaf.name
        other = True
        if seqid not in leaf_tags.keys():
            try:
                lineage = lineages[seqid]
                for tax_name in tax_names:
                    if tax_name in lineage:
                        leaf_tags[seqid] = tax_name
                        other = False
                if other: 
                    leaf_tags[seqid] = "other"
            except:
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

def check_hgt(target_node, leaf_tags, hgt_tag):
    if check_sisters_tag(target_node, leaf_tags, hgt_tag) and check_sisters_tag(target_node.up, leaf_tags, hgt_tag):
        return True
    return False

def get_group_node(target_leaf, leaf_tags, group_tag):
    node = target_leaf
    while check_sisters_tag(node, leaf_tags, group_tag):
        if node.up:
            node = node.up
        else: 
            return node
    else:
        return node

def write_lineage_tree(tree, outpath):
    smol_regex = "^g\d+\.t1"
    ncbi_seqids = []

    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if not re.match(smol_regex, seqid):
            ncbi_seqids.append(seqid)
    lineages = get_lineages_bulk(ncbi_seqids)

    for leaf in tree.iter_leaves():
        seqid = leaf.name
        if seqid in lineages.keys():
            lineage = lineages[seqid]
            leaf.name = lineage
    tree.write(outfile=outpath)
    return outpath

def analyse_tree(tree_path, hgt_tax_name, bootstrap_threshold=70.0, group_name=False):
    tree = Tree(tree_path)
    tree = remove_bad_nodes(tree, support_threshold=bootstrap_threshold)

    if group_name:
        tax_names = [hgt_tax_name, group_name]
    else:
        tax_names = [hgt_tax_name]

    leaf_tags = get_tags_leaves(tree, tax_names)
    target_leaf = None

    for leaf in tree.iter_leaves():
        if leaf_tags[leaf.name] == "smol":
            if not target_leaf:
                target_leaf = leaf
            else:
                print ("More than one smol leaf!\n" + tree_path + "\n")

    if not target_leaf:
        print ("No smol leaf!\n" + tree_path + "\n")

    farthest_node = target_leaf.get_farthest_node(topology_only=True)[0]

    if farthest_node.up == tree:
        result = False
    else:
        tree.set_outgroup(farthest_node.up)

    if group_name:
        group_node = get_group_node(target_leaf, leaf_tags, group_name)
        result = check_hgt(group_node, leaf_tags, hgt_tax_name)
    else:
        result = check_hgt(target_leaf, leaf_tags, hgt_tax_name)

    if result:
        outpath = tree_path + "_lin_hgt.tree"
    else:
        outpath = tree_path + "_lin_no.tree"
    write_lineage_tree(tree, outpath)
    
    return result

bootstrap_threshold = 70.0

treedir_path="/Users/vl18625/work/myxo_local/contrees/"
hgt_tax_name = "Vertebrata"

#treedir_path="/Users/annanenarokova/Google Drive/projects/myxozoans/hgt/hgt_candidates_old/fungi/contrees/"
#hgt_tax_name = "Fungi"

i = 0
for tree_name in listdir(treedir_path):
    tree_path = treedir_path + tree_name
    print (tree_name)
    is_hgt = analyse_tree(tree_path, hgt_tax_name, bootstrap_threshold=bootstrap_threshold)
    i += 1
    if i%10 == 0:
        print (i)
    if is_hgt:
        print ("hgt")
