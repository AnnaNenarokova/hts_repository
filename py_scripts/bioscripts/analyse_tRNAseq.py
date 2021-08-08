#!/usr/bin/python3
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def reverse(seq):
    complement = str.maketrans('ATGC', 'TACG')
    reverse = seq.translate(complement)[::-1]
    return reverse

def analyse_tRNAseq(tRNA_csv_path):
    tRNA_cluster_dicts = csv_to_list_of_dicts(tRNA_csv_path)
    tRNA_dict = {}
    for cluster_dict in tRNA_cluster_dicts:
        print (cluster_dict)
        size = int(cluster_dict["size"])
        amino_acid, anticodon = cluster_dict["best_blast_hit"].split("_")[0:2]
        anticodon = anticodon.upper()

        if amino_acid not in tRNA_dict:
            tRNA_dict[amino_acid] = {"aa_count": size, "anticodons": {anticodon:size}}
        else:
            tRNA_dict[amino_acid]["aa_count"] += size
            anticodons = tRNA_dict[amino_acid]["anticodons"]
            if anticodon not in anticodons:
                tRNA_dict[amino_acid]["anticodons"][anticodon] = size
            else:
                tRNA_dict[amino_acid]["anticodons"][anticodon] += size
    return tRNA_dict

def write_codons(tRNA_dict):
    for amino_acid in tRNA_dict:
        anticodons = tRNA_dict[amino_acid]["anticodons"]
        for anticodon in anticodons:
            print (anticodon, reverse(anticodon), amino_acid, anticodons[anticodon])
    return 0


tRNA_csv_path = "/Users/annanenarokova/work/blasto_local/tRNAseq/tbrucei/tRNA_clusters.csv"

tRNA_dict = analyse_tRNAseq(tRNA_csv_path)

write_codons(tRNA_dict)




