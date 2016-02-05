#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *
from database.nonspecific_functions import *

def filter_dic_list(dic_list, outhpath, fieldnames_list, filter_functions=True):
    results = []
    for dic in dic_list:
        if ( (dic['query_loc'] == 'M' and dic['query_locrate'] == 1)
            or
            ( (dic['query_mitoscore'] == 100) and ('double-stranded DNA binding;regulation of transcription' not in dic['query_function']) ) ):
            results.append(dic)
        elif (dic['query_og'] == dic['subject_og']) or (dic['subject_og'] == ''):
            is_specific = True
            if filter_functions:
                for function in nonspecific_functions:
                    if function.lower() in dic['subject_function'].lower() or function in dic['query_function'].lower():
                        is_specific = False
                        break
            if is_specific:
                results.append(dic)
    write_list_of_dicts(results, outpath, fieldnames=fieldnames_list)
    return outpath

an_path = '/home/anna/bioinformatics/phd/euglena_project/results_with_ogs.csv'

dic_list = csv_to_list_of_dicts(an_path)

fieldnames_list = ['query_id', 'query_function', 'query_mitoscore', 'query_loc', 'query_locrate', 'subject_id', 'subject_organism', 'subject_function', 'subject_loc', 'subject_locrate', 'evalue', 'qlen', 'slen', 'length', 'alen_slen', 'alen_qlen', 'query_og', 'subject_og']
outpath = '/home/anna/bioinformatics/phd/euglena_project/filtered_results_with_ogs.csv'

filter_dic_list(dic_list, outpath, fieldnames_list, filter_functions=True)