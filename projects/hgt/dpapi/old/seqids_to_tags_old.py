#!python
from ete3 import NCBITaxa
from ete3 import Tree
from Bio import Entrez
from os import listdir
Entrez.email = "a.nenarokova@gmail.com"

taxid_list_path="/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_from_trees.txt"
taxid_set_path="/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_set.txt"

def parse_taxids(taxid_path, delimeter="\t"):
    taxid_dict = {}
    with open(taxid_path) as taxid_file:
        for line in taxid_file:
            seqid, taxid = line.rstrip().split(delimeter)
            taxid_dict[seqid] = taxid
    return taxid_dict

def get_seqid_set(tree_dir):
    seqid_set = set()
    for tree_name in listdir(tree_dir):
        tree_path = tree_dir + tree_name
        tree = Tree(tree_path)
        for leaf in tree.iter_leaves():
            seqid_set.add(leaf.name)
    return list(seqid_set)

def get_seqid_taxid_dict(seqids, taxid_dict):
    seqid_taxid_dict = {}
    taxid_keys = taxid_dict.keys()
    for seqid in seqids:
        if "DIPPA" in seqid:
            pass
        elif seqid in taxid_keys:
            seqid_taxid_dict[seqid] = taxid_dict[seqid]
        else:
            print seqid, "is not in taxid_dict!"
    return seqid_taxid_dict

def get_taxid_set(seqid_taxid_dict):
    taxid_set = set()
    for seqid in seqid_taxid_dict:
        if "DIPPA" in seqid:
            pass
        else:
            taxid_set.add(seqid_taxid_dict[seqid])
    return list(taxid_set)

def taxids_to_tags(taxids, ncbi_taxa):
    bacteria_taxid = 2
    diplonemid_taxid = 191814
    taxid_tag_dict = {}
    for taxid_str in taxids:
        taxid = int(taxid_str)
        tag = "other"
        bad_taxids = [2005002]
        if (taxid not in bad_taxids) and (taxid < 2447898):
            lineage = ncbi_taxa.get_lineage(taxid)
            if bacteria_taxid in lineage:
                tag = "bacteria"
            elif diplonemid_taxid in lineage:
                tag = "diplonemid"
        else:
            entrez_handle = Entrez.efetch(db="taxonomy", id=taxid)
            data_parsed = Entrez.read(entrez_handle)
            lineage = data_parsed[0]["Lineage"].split("; ")
            lineage_len = len(lineage)
            if lineage_len > 1:
                if lineage[1] == "Bacteria":
                    tag = "bacteria"
                elif lineage_len > 3 :
                    if lineage[3] == "Diplonemea":
                        tag = "diplonemid"
        taxid_tag_dict[taxid_str] = tag
    return taxid_tag_dict

tree_dir="/home/anna/bioinformatics/diplonema/hgt/results_last/trees/"

taxid_path = "/home/anna/bioinformatics/diplonema/hgt/results_last/selected_seqids_taxids.txt"

# taxid_path="/home/anna/bioinformatics/diplonema/hgt/whole_taxids_no_problem.csv"

tag_outpath = "/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_tags.tsv"

taxid_dict = parse_taxids(taxid_path)
print "taxid_dict done! length =", len(taxid_dict)

seqid_set = get_seqid_set(tree_dir)
print "seqid_set done! length =", len(seqid_set)

selected_taxid_dict = get_seqid_taxid_dict(seqid_set, taxid_dict)
print "selected_taxid_dict done!"
selected_outpath = "/home/anna/bioinformatics/diplonema/hgt/results_last/selected_seqids_taxids2.txt"

with open(selected_outpath, "w") as outfile:
    for seqid in selected_taxid_dict:
        outfile.write(seqid + "\t" + selected_taxid_dict[seqid] + "\n")


taxid_set = get_taxid_set(selected_taxid_dict)
print "taxid_set done!"

ncbi_taxa = NCBITaxa()

taxid_tag_dict = taxids_to_tags(taxid_set, ncbi_taxa)
print "taxid_tag_dict done!"

with open (tag_outpath, "w") as tag_outfile:
    taxid_keys = selected_taxid_dict.keys()
    for seqid in selected_taxid_dict:
        if "DIPPA" in seqid:
            tag = "dpapi"
        elif seqid in taxid_keys:
            tag = taxid_tag_dict[selected_taxid_dict[seqid]]
        else:
            tag = "other"
        tag_outfile.write(seqid + "\t" + tag + "\n")
