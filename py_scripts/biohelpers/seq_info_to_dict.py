#!/usr/bin/python
import csv

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