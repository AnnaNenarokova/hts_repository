#!/usr/bin/python3
import sys
sys.path.insert(0, '/Users/annanenarokova/work/code/ngs/')
from py_scripts.helpers.parse_csv import *

def get_pfam_result_dict(pfam_path):
    pfam_list = csv_to_list_of_dicts(pfam_path, delimiter=';')
    pfam_dict = {}
    for row in pfam_list:
        query_name = row['query_name']
        if query_name not in pfam_dict:
            pfam_dict[query_name] = []
        pfam_dict[query_name].append(row)
    return pfam_dict

def get_best_pfam_hit(pfam_hit_list):
    best_pfam_hit = pfam_hit_list[0]

    for pfam_hit in pfam_hit_list:
        current_evalue = float(pfam_hit['E-value'].replace(",","."))
        best_evalue = float(best_pfam_hit['E-value'].replace(",","."))
        current_GO = pfam_hit['GO']
        best_GO = best_pfam_hit['GO']

        if best_GO == '#N/A':
            if current_GO == '#N/A':
                if current_evalue < best_evalue:
                    best_pfam_hit = pfam_hit
            else:
                best_pfam_hit = pfam_hit
        elif current_GO != '#N/A' and current_evalue < best_evalue:
            best_pfam_hit = pfam_hit

    return best_pfam_hit

def get_best_pfam_hits(pfam_path):
    pfam_dict = get_pfam_result_dict(pfam_path)
    best_pfam_hits = []
    for query in pfam_dict:
        best_hit = get_best_pfam_hit(pfam_dict[query])
        best_pfam_hits.append(best_hit)
    return best_pfam_hits

pfam_path = '/Users/annanenarokova/work/myxo/pfam_go_terms.csv'
outpath = '/Users/annanenarokova/work/myxo/best_pfam_hits.csv'

best_pfam_hits = get_best_pfam_hits(pfam_path)

write_list_of_dicts(best_pfam_hits, outpath)