#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from py_scripts.biohelpers.analyse_taxa import *
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def parse_taxids(taxid_path, delimeter=","):
    seq_taxid_dict = {}
    seq_dict_list = csv_to_list_of_dicts(taxid_path, delimiter=',')
    for dic in seq_dict_list:
        seqid = dic['new_id']
        taxid = dic['taxid']
        if seqid !='new_id':
            seq_taxid_dict[seqid] = taxid
    return seq_taxid_dict

def taxids_to_tags(taxid_dict, tag_list):
    taxid_tag_dict = {}
    for taxid in taxid_dict:
        lineage = taxid_dict[taxid]["lineage"]
        tag_found = False
        for tag in tag_list:
            if tag in lineage:
                tag_found = True
                taxid_tag_dict[taxid] = tag
                break
        if not tag_found:
            tag = "other"
            taxid_tag_dict[taxid] = tag
    return taxid_tag_dict

def write_tags(seq_taxid_dict, taxid_tag_dict, outpath):
    with open(outpath, 'w') as outfile:
        for seqid in seq_taxid_dict:
            taxid = seq_taxid_dict[seqid]
            tag = taxid_tag_dict[taxid]
            outfile.write(seqid + "\t" + tag + "\n")
    return outpath

def get_tags(taxid_info_path, outpath, tag_list):
    print ("Parcing the taxid info file")
    seq_taxid_dict = parse_taxids(taxid_info_path)
    taxid_set = get_taxid_set(seq_taxid_dict)
    taxid_dict = get_taxid_dict(taxid_set)
    taxid_tag_dict = taxids_to_tags(taxid_dict, tag_list)
    print ("Writing down the results")
    write_seq_tags(taxid_tag_dict, outpath, tag_list)
    return outpath

tag_list = ["Bacteria", "Diplonemea"]

