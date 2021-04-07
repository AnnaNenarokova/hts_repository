#!python3
import os
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from py_scripts.biohelpers.analyse_taxa import *
from py_scripts.biohelpers.get_records import *

def get_hgt_candidate_list(diamond_taxa_result_path, taxon="Bacteria"):
    seq_tax_dict = get_seq_lineages(diamond_taxa_result_path)
    candidate_list = []
    for seqid in seq_tax_dict:
        if taxon in seq_tax_dict[seqid]["lineage"]:
            candidate_list.append(seqid)
    return candidate_list

def get_hgt_candidates(diamond_taxa_result_path, infasta, outfasta):
    candidate_list = get_hgt_candidate_list(diamond_taxa_result_path)
    keep_from_list(infasta, candidate_list, outfasta)
    return 0 

diamond_taxa_result_path="/Users/annanenarokova/work/dpapi_local/dpapi_recoded_nr_tax.tsv"
infasta="/Users/annanenarokova/work/dpapi_local/dpapi_recoded_for_refset.faa"
outfasta="/Users/annanenarokova/work/dpapi_local/dpapi_recoded_hgt_cands.faa"

get_hgt_candidates(diamond_taxa_result_path, infasta, outfasta)