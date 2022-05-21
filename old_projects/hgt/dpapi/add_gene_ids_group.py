#!python3
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from py_scripts.helpers.parse_csv import *

def add_gene_ids(hgt_ids_file, geneid_path, outpath):
    hgt_dict_list = csv_to_list_of_dicts(hgt_ids_file, delimiter='\t')
    result_dict = {}
    id_dict = csv_to_dict(geneid_path, main_key="new_id", delimiter=';')
    for dic in hgt_dict_list:
        hgt_group_id = dic["hgt_id_group"]
        gene_id = dic["gene_id"]
        if gene_id in id_dict.keys():
            gene_id = id_dict[gene_id]["old_id"]
        if hgt_group_id not in result_dict.keys():
            result_dict[hgt_group_id] = [gene_id]
        else:
            result_dict[hgt_group_id].append(gene_id)
    with open(outpath, 'w') as csv_file:  
        writer = csv.writer(csv_file)
        writer.writerow(["hgt_group_id", "length", "gene_ids"])
        for hgt_group_id, hgt_group in result_dict.items():
            hgt_group_len = str(len(hgt_group))
            hgt_group_combined = ", ".join(sorted(hgt_group))
            writer.writerow([hgt_group_id, hgt_group_len, hgt_group_combined])
    return outpath

hgt_ids_file = "/Users/annanenarokova/work/dpapi_local/results_16_08/hgt_ids.tsv"
geneid_path = "/Users/annanenarokova/work/dpapi_local/dpapi_info.csv"
outpath = "/Users/annanenarokova/work/dpapi_local/results_16_08/hgt_group_gene_ids.tsv"

add_gene_ids(hgt_ids_file, geneid_path, outpath)