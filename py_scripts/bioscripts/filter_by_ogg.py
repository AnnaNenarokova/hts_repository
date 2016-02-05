#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *

an_path = '/home/anna/bioinformatics/phd/euglena_project/results_with_ogs.csv'

dic_list = csv_to_list_of_dicts(an_path)

results = []

for dic in dic_list:
    if (dic['query_og'] == dic['subject_og']) or (dic['subject_og'] == '') or (dic['query_loc'] == 'M' and dic['query_locrate'] == 1):
        results.append(dic)

outpath = '/home/anna/bioinformatics/phd/euglena_project/filtered_results_with_ogs.csv'

fieldnames_list = ['query_id', 'query_function', 'query_mitoscore', 'query_loc', 'query_locrate', 'subject_id', 'subject_organism', 'subject_function', 'subject_loc', 'subject_locrate', 'evalue', 'qlen', 'slen', 'length', 'alen_slen', 'alen_qlen', 'query_og', 'subject_og']
write_list_of_dicts(results, outpath, fieldnames=fieldnames_list)