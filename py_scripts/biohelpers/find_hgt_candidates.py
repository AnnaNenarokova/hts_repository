#!python3
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.biohelpers.analyse_taxa import *
from py_scripts.biohelpers.get_records import *

def find_hgt_candidates(diamond_taxa_result_path, infasta_path, hgt_taxon="Bacteria", outfasta_path=False, evalue_cutoff=1):
    if not outfasta_path:
        outfasta_path = infasta_path + ".hgt_candidates.fa"
    taxid_dict, seq_dict = get_taxid_dicts(diamond_taxa_result_path)
    hgt_candidates_seq_list = []
    for seq in seq_dict:
        if seq_dict[seq]["evalue"] < evalue_cutoff:
            taxid = seq_dict[seq]["taxid"]
            if hgt_taxon in taxid_dict[taxid]["lineage"]:
                hgt_candidates_seq_list.append(seq)
    keep_from_list(infasta_path, hgt_candidates_seq_list, outfasta_path)
    return outfasta_path