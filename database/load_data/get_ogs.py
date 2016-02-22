#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *

def get_ogs(csv_path, og_path, outpath, organism):
    og_dict = csv_to_dict_reverse(csv_path)
    print og_dict.keys()
    csv_list = csv_to_list_of_dicts(csv_path)
    for dic in csv_list:
        seqid = dic['seqid']
    return 0

def get_homo_ogs(csv_path, og_path, ids_to_ccds_path):
    return 0

og_path = '/home/anna/Dropbox/phd/db/proteomes/parsed_ortho_groups.csv'

ids_to_ccds_path = '/home/anna/Dropbox/phd/db/proteomes/homo/data/ids_to_ccds.csv'

csv_path = '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.csv'
outpath = '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito_ogs.csv'

get_ogs(csv_path, og_path, outpath, organism='Giardia intestinalis')