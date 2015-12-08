#!/usr/bin/python
import csv
def parse_csv(csv_path, delimiter=','):
	with open(csv_path) as handle_file:
		handle_csv = csv.reader(handle_file, delimiter=delimiter)
		results = []
		for row in handle_csv:
			results.append(row)
		handle_file.close()
	return results

def csv_to_dict(csv_path):
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel')
        csv_dict = []
    	for row in reader:
        	csv_dict.append(row)
        csvfile.close
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