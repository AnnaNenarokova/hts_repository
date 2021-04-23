#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from py_scripts.biohelpers.analyse_taxa import *

def parse_taxids(taxid_path, delimeter="\t"):
    seq_taxid_dict = {}
    with open(taxid_path) as taxid_file:
        for line in taxid_file:
            line_split = line.rstrip().split(delimeter)
            seqid = line_split[0]
            if len(line_split) == 2:
                taxid = line_split[1]
            else:
                taxid = "0"
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

def get_tags(seqid_taxid_path, outpath, tag_list):
    seq_taxid_dict = parse_taxids(seqid_taxid_path)
    taxid_set = get_taxid_set(seq_taxid_dict)
    taxid_dict = get_taxid_dict(taxid_set)
    taxid_tag_dict = taxids_to_tags(taxid_dict, tag_list)
    print ("Writing down the results")
    with open(outpath, 'w') as outfile:
        for seq in seq_taxid_dict:
            taxid = seq_taxid_dict[seq]
            if taxid in taxid_tag_dict.keys():
                tag = taxid_tag_dict[taxid]
            else:
                print (taxid, "is not in taxid_tag_dict!")
                tag = "other"
            outfile.write(seq + "\t" + tag + "\n")
    return outpath

tag_list = ["Bacteria", "Diplonemea"]

seqid_taxid_path = "/Users/annanenarokova/work/dpapi_local/test_dmd_extracted_taxids.tsv"
outpath = "/Users/annanenarokova/work/dpapi_local/seqs_tags.tsv"

get_tags(seqid_taxid_path, outpath, tag_list)
