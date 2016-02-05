#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *

an_path = '/home/anna/bioinformatics/phd/euglena_project/results_with_ogs.csv'

dic_list = csv_to_list_of_dicts(an_path)

results = []

for dic in dic_list:
    if (dic['query_og'] == dic['subject_og']) or ('subject_og' == '') or (dic['query_loc'] == 'M' and dic['query_locrate'] == 1):
        results.append(dic)

outpath = '/home/anna/bioinformatics/phd/euglena_project/filtered_results_with_ogs.csv'

write_list_of_dicts(results, outpath)