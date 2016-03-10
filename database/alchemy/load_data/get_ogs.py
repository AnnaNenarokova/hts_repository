#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *

def get_ogs_from_dict(csv_path, og_dicts, organism, outpath=False):
    print organism
    if not outpath: outpath = csv_path[0:-4] + '_ogs.csv'
    og_dict = og_dicts[organism]
    csv_list = csv_to_list_of_dicts(csv_path)
    i = 0
    for og in og_dict:
        if i%10000 == 0: print i
        i+=1
        for dic in csv_list:
            seqid = dic['seqid']
            if seqid in og_dict[og]:
                dic['og'] = og
    fieldnames = ['seqid', 'og', 'function', 'mitochondrial']
    write_list_of_dicts(csv_list, outpath, fieldnames)
    return 0

def get_homo_ogs(csv_path, og_path, ids_to_ccds_path, outpath=False):
    print 'Homo sapiens'
    if not outpath: outpath = csv_path[0:-4] + '_ogs.csv'
    og_dict = csv_to_dict_reverse(og_dicts)
    ids_to_ccds = csv_to_dict(ids_to_ccds_path, main_key='Entry')
    i = 0
    for dic in csv_list:
        if i%100 == 0: print i
        i+=1
        seqid = dic['seqid']
        ccds = ids_to_ccds[seqid]['CCDS ID'].split(';')
        if len(ccds[0]) == 0:
            dic['og'] = ''
        else:
            has_og = False
            if not has_og:
                for og in og_dict:
                    if has_og: break
                    for ccd in ccds:
                        if ccd in og_dict[og]:
                            dic['og'] = og
                            has_og = True
                            break
    fieldnames = ['seqid', 'og', 'function', 'mitochondrial']
    write_list_of_dicts(csv_list, outpath, fieldnames)
    return 0

def get_ogs(data_paths, og_path, ids_to_ccds_path):
    og_dicts = csv_to_dict_reverse(og_path)
    for organism in data_paths:
        if organism == 'Homo sapiens':
            get_homo_ogs(data_paths[organism], og_dicts, ids_to_ccds_path)
        else:
           get_ogs_from_dict(data_paths[organism], og_dicts, organism)


og_path = '/home/anna/Dropbox/phd/db/proteomes/parsed_ortho_groups.csv'



csv_path = '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.csv'
outpath = '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito_ogs.csv'

data_paths = {
    'Arabidopsis thaliana': '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis_mito.csv',
    'Giardia intestinalis': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.csv',
    'Euglena gracilis': '/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins.csv',
    'Homo sapiens': '/home/anna/Dropbox/phd/db/proteomes/homo/data/human_mito.csv',
    'Saccharomyces cerevisiae': '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.csv',
    'Trichomonas vaginalis': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito.csv',
    'Trypanosoma brucei': '/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma_mito.csv'
        }

# get_ogs(data_paths, og_path)
og_path = '/home/anna/Dropbox/phd/db/proteomes/homo/data/homo_ogs.csv'
ids_to_ccds_path = '/home/anna/Dropbox/phd/db/proteomes/homo/data/ids_to_ccds.csv'
csv_path = '/home/anna/Dropbox/phd/db/proteomes/homo/data/human_mito.csv'
