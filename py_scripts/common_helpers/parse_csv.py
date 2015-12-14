#!/usr/bin/python
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.dict_list_to_dict import *

def parse_csv(csv_path, delimiter=','):
	with open(csv_path) as handle_file:
		handle_csv = csv.reader(handle_file, delimiter=delimiter)
		results = []
		for row in handle_csv:
			results.append(row)
		handle_file.close()
	return results

def csv_to_dict_list(csv_path):
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel')
        dict_list = []
    	for row in reader:
        	dict_list.append(row)
        csvfile.close
    return dict_list

def csv_to_dict(csv_path, main_key):
    dict_list = csv_to_dict_list(csv_path)
    csv_dict = dict_list_to_dict(dict_list, main_key)
    return csv_dict

def write_dicts_list(dict_list, outfile):
	with open(outfile, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=dict_list[0].keys())
		writer.writeheader()
		for row in dict_list:
			writer.writerow(row)
		csvfile.close()
	return outfile

def write_dicts_dict(dicts_dict, outfile, key_name='name'):
	dicts_list = []
	for key in dicts_dict:
		cur_dict = {}
		cur_dict[key_name] = key
		for k in dicts_dict[key]:
			cur_dict[k] = dicts_dict[key][k]
		dicts_list.append(cur_dict)
	write_dicts_list(dicts_list, outfile)
	return outfile