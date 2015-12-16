#!/usr/bin/python
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.common_helpers.parse_csv import *

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