#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.parse_csv import *

def seq_info_to_dict(csv_path):
    with open(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)
        result = {}
        for row in reader:
            result[row['seqid']] = {}
            for key in row:
                if key != 'seqid': result[row['seqid']][key] = row[key]
        csv_file.close()
    return result

def b2g_to_functions(b2g_dict):
    result = {}
    for seqid in b2g_dict:
        function = b2g_dict[seqid]['SeqDesc']  + ', ' +  b2g_dict[seqid]['GOTerms']
        result[seqid] = {}
        result[seqid]['function'] = function
    return result

csv_path = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast2go_annotdescriptions_20151104_1903.csv'

seq_info_dict = seq_info_to_dict(csv_path)

seq_info_dict = b2g_to_functions(seq_info_dict)
