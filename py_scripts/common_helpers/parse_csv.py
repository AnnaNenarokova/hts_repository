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

def write_dict_list(dict_list, outfile):
	with open(outfile, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=dict_list[0].keys())
		writer.writeheader()
		for row in dict_list:
			writer.writerow(row)
		csvfile.close()